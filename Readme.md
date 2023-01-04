
# Mutual Authentication Using ECQC  
  
ECQV certificates are lightweight alternatives to the classical X509 certificates and are typically used in IoT applications. In addition, they have interesting security features, as they do not need a secure channel between the certificate authority (CA) and the device requesting a certificate. In addition, they offer protection against key escrow attacks, as the CA is also not aware of the private key established by the device during the protocol.  
[[1]](#1)  
  
  
## Protocol Details  
from [[2]](#2)
This scheme is composed in three main phases  
1. [Implicit certificate generation phase](img/Phase1.md)
+ 1.1  Implicit Certificate Request  
+ 1.2  Implicit Certificate Generation  
+ 1.3  Certificate Public Key Extraction
2. [Pair wise key establishment phase](img/Phase2.md)   
3. [Mutual authentication phase](img/Phase3.md)  
  
***  
# References  
<a id="1">[1]</a>  Porambage, Pawani, et al. "Certificate-based pairwise key establishment protocol for wireless sensor networks." 2013 IEEE 16th International Conference on Computational Science and Engineering. IEEE, 2013.  

  
<a id="2">[2]</a>  Siddhartha, Valmiki, Gurjot Singh Gaba, and Lavish Kansal. "A lightweight authentication protocol using implicit certificates for securing iot systems." Procedia Computer Science 167 (2020): 85-96.  

  
<a id="3">[3]</a>  Sciancalepore, Savio, et al. "Public key authentication and key agreement in IoT devices with minimal airtime consumption." IEEE Embedded Systems Letters 9.1 (2016): 1-4.  

  
<a id="4">[4]</a>  Campagna, Matthew. "SEC 4: Elliptic Curve Qu-Vanstone implicit certificate scheme (ECQV)." Standards for Efficient Cryptography, Version 1 (2013).  

  
<a id="5">[5]</a>  Park, Chang-Seop. "A secure and efficient ECQV implicit certificate issuance protocol for the internet of things applications." IEEE Sensors Journal 17.7 (2016): 2215-2223.  

  
<a id="6">[6]</a>  Kwon, Hee-Yong, and Mun-Kyu Lee. "Fast verification of signatures with shared ECQV implicit certificates." IEEE Transactions on Vehicular Technology 68.5 (2019): 4680-4694. 
 
  
<a id="7">[7]</a>  Basic, Fikret, Christian Steger, and Robert Kofler. "Poster: Establishing Dynamic Secure Sessions for Intra-Vehicle Communication Using Implicit Certificates." International Conference on Embedded Wireless Systems and Networks (EWSN) 2022. 2022.
