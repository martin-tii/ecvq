import random

from fastecdsa import curve, keys
import ca
from cert_generation import  cert_request, cert_Reception
import pair_wise_key_establishment as pks
from termcolor import colored

CURVE = curve.secp256k1


def same(key1, key2):
    if key1 == key2:
        return True
    print("different keys")
    return False

def calculate_hash(value):
    return hash(value)

def authenticate(**args):
    value = ''.join(args.values())
    hashed = calculate_hash(value)
    return args.values(), hashed


def send2othernode(values, hashed):
    pass

def validate_hash(values, hashed, key):
    _, hashed2 = authenticate(node1=values[0],node2=values[1],nonce=values[2],key=str(key))
    if hashed == hashed2:
        print(colored("Authenticated","green"))
    else:
        print(colored("Not Authenticated", "red"))


if __name__ == "__main__":
    CAPrivkey, CAPubKey = keys.gen_keypair(CURVE) #this should be generated on the CA

    #for node U
    request, alpha = cert_request() # for each node (alpha must be private)
    privKey_cont, cert_u = ca.cert_generate("nodeU", request, CAPrivkey)
    priv_key_u, pub_key_u = cert_Reception("nodeU", alpha, privKey_cont, cert_u, CAPubKey)

    # for node V
    request_v, alpha_v = cert_request() # for each node (alpha must be private)
    privKey_cont_v, cert_v = ca.cert_generate("nodeV", request_v, CAPrivkey)
    priv_key_v, pub_key_v = cert_Reception("nodeV", alpha_v, privKey_cont_v, cert_v, CAPubKey)


    kuv = pks.shared_secret("nodeU", cert_u, priv_key_v, CAPubKey)
    kvu = pks.shared_secret("nodeV", cert_v, priv_key_u, CAPubKey)
    assert same(kvu, kuv)


    nonce = random.randint(1,99)
    values, hashed = authenticate(node1="nodeU", node2="nodeV", nonce=str(random.randint(1,99999999999999999)), key=str(kuv))
    print(values)
    print(hashed)

#    send2othernode(list(values)[0:-1], hashed)
    validate_hash(list(values)[0:-1], hashed, kvu)

