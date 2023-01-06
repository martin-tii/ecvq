from fastecdsa import curve, keys
import random

CURVE = curve.secp256k1


def cert_generate(idText, request, CAPrivkey):
    """
    A certificate authority (CA) generates an implicit certificate using
    identity string @id, @request (certificate public key component), and
    the CA's private key @caPrivkey.
    @returns (s, cert) where @r is the private key contribution and @cert is
     the implicit certificate.
    """

    # 2  need to validate R_u (request)

    R = request
    d = CAPrivkey
    G = CURVE.G
    N = CURVE.q #order of G


    # Random integer
    k = random.randint(1,N)
    kG = k*G
    P = R + kG #this is the certificate
    e = hash(str(P) + idText) # I'm not sure if this is correct

    # Compute the private key contribution
    r = (e*k + d) % N
    return r, P

    '''
    binding a public key to its owner in a trusted way, make the proposed strategy robust against man-in-the-middle (MITM) attacks.
    '''
