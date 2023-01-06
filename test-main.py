import random
import hmac
from fastecdsa import curve, keys
import ca
from cert_generation import  cert_request, cert_Reception
import pair_wise_key_establishment as pks
from termcolor import colored
from ecies import encrypt, decrypt
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

CURVE = curve.secp256k1


def same(key1, key2):
    if key1 == key2:
        return True
    print("different keys")
    return False

def calculate_hash(value):
    return hash(value)

def authenticate(**args):
    '''
    each authentication tag is computed by including all the information exchanged in the first two messages
    (plus the peer identities) and hence protects the entire exchange from MITM modifications
    '''
    value = ''.join(args.values())
    hashed = calculate_hash(value)
    return args.values(), hashed
    '''
    protects the entire approach against replay attacks, and explicitly binds the exchanged cryptographic 
    quantities to the involved peer identities using per-session nonces
    '''


def send2othernode(values, hashed):
    raise NotImplementedError


def validate_hash(values, hashed, key):
    _, hashed2 = authenticate(node1=values[0],node2=values[1],nonce=values[2],key=str(key))
    if hashed == hashed2:
        print(colored("Authenticated","green"))
    else:
        print(colored("Not Authenticated", "red"))


def encodeKey(CAPubKey, symmetric=True):
    uncompressed_key_hex = '04' + hex(CAPubKey.x)[2:] + hex(CAPubKey.y)[2:]
    uncompressed_key = bytes.fromhex(uncompressed_key_hex)
    if symmetric:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(uncompressed_key))
        return  Fernet(key)
    else: return uncompressed_key

def symEncrypt(key, message, HMAC=False):
    '''
    maybe we can think to use HMAC instead
    '''
    if HMAC:
        hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod='sha256')
        return hmac1.digest()
    return key.encrypt(message)

def asymEncrypt(Pubkey, message):
    return encrypt(Pubkey,message)

def symDecryt(key, encrypted):
    return key.decrypt(encrypted)

def asymEncrypt(PrivKey, encrMessage):
    return decrypt(hex(PrivKey), encrMessage)

if __name__ == "__main__":
    CAPrivkey, CAPubKey = keys.gen_keypair(CURVE) #this should be generated on the CA

    #for node U
    idnode1 = "nodeU"
    request, alpha = cert_request() # for each node (alpha must be private)
    privKey_cont, cert_u = ca.cert_generate(idnode1, request, CAPrivkey)
    priv_key_u, pub_key_u = cert_Reception(idnode1, alpha, privKey_cont, cert_u, CAPubKey)

    # for node V
    idnode2="nodeV"
    request_v, alpha_v = cert_request() # for each node (alpha must be private)
    privKey_cont_v, cert_v = ca.cert_generate(idnode2, request_v, CAPrivkey)
    priv_key_v, pub_key_v = cert_Reception(idnode2, alpha_v, privKey_cont_v, cert_v, CAPubKey)


    kuv = pks.shared_secret(idnode1, cert_u, priv_key_v, CAPubKey)
    kvu = pks.shared_secret(idnode2, cert_v, priv_key_u, CAPubKey)
    assert same(kvu, kuv)

    nonce = str(random.randint(1,99999999999999999)) #this nonce should be created for every new session
    values, hashed = authenticate(node1=idnode1, node2=idnode2, nonce=nonce, key=str(kuv))
    print(values)
    print(hashed)

#    send2othernode(list(values)[0:-1], hashed)
    validate_hash(list(values)[:-1], hashed, kvu)
