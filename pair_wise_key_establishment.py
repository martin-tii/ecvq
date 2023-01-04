from fastecdsa import curve
from cert_generation import cert_PK_Extraction

CURVE = curve.secp256k1


def shared_secret(remoteId, cert, myPrivKey, caPubKey):
    pubkey_remote = cert_PK_Extraction(remoteId, cert, caPubKey)
    return myPrivKey*pubkey_remote
