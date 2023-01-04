from fastecdsa import curve
import random

CURVE = curve.secp256k1


def cert_request():
    # Curve parameters
    n = CURVE.q
    k_u = random.randint(1, n)
    R_u = k_u * CURVE.G #request
    return R_u, k_u


def cert_Reception(idText, k_u, r, cert, caPubkey):
    """
    A server can validate an implicit certificate response using identity
    string @idText, private value @k_u (used to generate cert request),
    and the certificate response @r (private key component) and implicit
    @cert.
    @raises Exception if the certificate response is invalid.
    @returns (privkey, pubkey)
    """


    G = CURVE.G

    # Compute the private key @s
    e = hash(str(cert)+idText)
    s = (e*k_u + r) % CURVE.q

    # Compute the public key two ways: using the privkey and using the cert
    # (the way a client will compute it)
    # The easy way
    S1 = s*G
    # Using the cert
    S2 = cert_PK_Extraction(idText, cert, caPubkey)

    # The two techniques should produce the same pubkey value -- raise an
    # exception if they don't match
    if S1 != S2:
        raise Exception("Implicit certification response failed validation")
    return s, S1


def cert_PK_Extraction(idText, cert, caPubkey):
    """
    A client can recover the server's pubkey using the identity string @idText,
    server's implicit @cert, and the trusted @caPubkey.
    """
    # Compute the pubkey
    return hash(str(cert)+idText)*cert + caPubkey
