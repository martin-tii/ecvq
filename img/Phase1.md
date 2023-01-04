### 1.1 Implicit Certificate Request  
**Input:**

1. The elliptic curve domain parameters established by CA  
2. A string $U$ representing U’s identity  
  
  
[![figure](https://mermaid.ink/img/pako:eNp1UctOwzAQ_BVrT4BC1cR5NJaoVAUJLlSo0AuEg-tsWovEKY4tUar-O5sGTggfrNXszOxo9wiqqxAE9Pjh0Si81XJrZVsaRu9ZuwZZgdbpWivpkK0GWu_G9l5SQ-m9NI4tyWb9Fy4WpRnRZUfyBmvHunpkC_ao1TtbSVN1LTO-3aAVzHr2v6CQjfINBRFs5dkNka_uRrZF5Zjdbi7CPAxYFHH6kuTy14rU1_N5sRh0AVsH7F72u1eq128jBU0FAbRoW6kr2sdxgEtwO2yxBEFlhbX0jSuhNCeiSu-6p4NRIJz1GIDfV5TrZ30gatn0hNISQBzhEwRPokmUx3nOk2ka5xkP4EDojE_SKEuzacR5loV5fArgq-vIYTrJkpCH8SybxSnP4iQMACvtOvswnux8ufOIl7NgyHH6BjWujxQ?type=png)](https://mermaid.live/edit#pako:eNp1UctOwzAQ_BVrT4BC1cR5NJaoVAUJLlSo0AuEg-tsWovEKY4tUar-O5sGTggfrNXszOxo9wiqqxAE9Pjh0Si81XJrZVsaRu9ZuwZZgdbpWivpkK0GWu_G9l5SQ-m9NI4tyWb9Fy4WpRnRZUfyBmvHunpkC_ao1TtbSVN1LTO-3aAVzHr2v6CQjfINBRFs5dkNka_uRrZF5Zjdbi7CPAxYFHH6kuTy14rU1_N5sRh0AVsH7F72u1eq128jBU0FAbRoW6kr2sdxgEtwO2yxBEFlhbX0jSuhNCeiSu-6p4NRIJz1GIDfV5TrZ30gatn0hNISQBzhEwRPokmUx3nOk2ka5xkP4EDojE_SKEuzacR5loV5fArgq-vIYTrJkpCH8SybxSnP4iQMACvtOvswnux8ufOIl7NgyHH6BjWujxQ)

**Output:** The key $k_U$ and the certificate request $(U, R_u)$.  
  
### 1.2 Implicit Certificate Generation  
**Input:** 

1. The elliptic curve domain parameters established by CA  
2. The hash function H selected by CA   
3. CA’s private key $d_{ca}$  
4. The certificate request  $(U, R_u)$.  
  
 [![](https://mermaid.ink/img/pako:eNp1kk1v2zAMhv-KoFOSKkb8FccGGiDIhuywFVub9NC6B9WiE2G2lMkSsDTIfx_90cPQxgfBIB--fEXxTAstgGa0gT8OVAFfJN8bXueK4LeVtgKyBmNlKQtugWxAgeFWatUTR465Qh65suQOlXYfw-tVPsDrFZku8czII6-kaPV2HzJgZHki33hz6FN3GjEj9wdLdNkhP2XxmxiuhK6JcvUrGGJQ4NlnnucxNfVfrlUWeBNHbsm9IzdtzWRzjQSkWg-jrmR8DTOIwaTtfkMEnqNaC6IG3EBhidm_jvzUZyQIQjziePx-4-ly2U0sIytnD7vbr8-o0PdjDds-sO9bdu_YbvzCeisdNpSDEu-eUKId3qD1-fwqKDvPAyRc77sdQ_O_6c_wXy0u3GRDGa3B1FwK3JhzW5BTe4Aacprhr4CSu8rmNFcXRLmz-uGkCppZ44BRd2yffFgwmpW8ajCKO0KzM_1LszAOvCCN0jSMZ_MoTUJGTxhdhN48SObJLAjDJPHT6MLom9aoMPOS2A_9aJEsonmYRLHPKAhptfnRL3W3212Lp66g9XH5B9It4pU?type=png)](https://mermaid.live/edit#pako:eNp1kk1v2zAMhv-KoFOSKkb8FccGGiDIhuywFVub9NC6B9WiE2G2lMkSsDTIfx_90cPQxgfBIB--fEXxTAstgGa0gT8OVAFfJN8bXueK4LeVtgKyBmNlKQtugWxAgeFWatUTR465Qh65suQOlXYfw-tVPsDrFZku8czII6-kaPV2HzJgZHki33hz6FN3GjEj9wdLdNkhP2XxmxiuhK6JcvUrGGJQ4NlnnucxNfVfrlUWeBNHbsm9IzdtzWRzjQSkWg-jrmR8DTOIwaTtfkMEnqNaC6IG3EBhidm_jvzUZyQIQjziePx-4-ly2U0sIytnD7vbr8-o0PdjDds-sO9bdu_YbvzCeisdNpSDEu-eUKId3qD1-fwqKDvPAyRc77sdQ_O_6c_wXy0u3GRDGa3B1FwK3JhzW5BTe4Aacprhr4CSu8rmNFcXRLmz-uGkCppZ44BRd2yffFgwmpW8ajCKO0KzM_1LszAOvCCN0jSMZ_MoTUJGTxhdhN48SObJLAjDJPHT6MLom9aoMPOS2A_9aJEsonmYRLHPKAhptfnRL3W3212Lp66g9XH5B9It4pU)
 
**Output:**  The Implicit certificate is generated from $R_u$, $r_{ca}$ and $G$, where as implicit signature is generated from hash of the certificate $U$, and private key of the  
certification authority,$d_{ca}$. The private key of the CA ($d_{CA}$), is used to encrypt the details ($Cert_U$,$r$,$Timestamp(TS)$, $Lifetime(LT)$,$R_u$,$U$) of the  
node U. This is called the authenticator ($Auth_u$).  

### 1.3 Certificate Public Key Extraction 

**Input** 

1. The elliptic curve domain parameters established by CA  
2. The authenticator $Auth_u$

[![](https://mermaid.ink/img/pako:eNp1kE9Lw0AQxb_KMCetsSRNm6QLClKhXhTEPwfZy5Kd2IVkN252wRry3d0k7Umc0zDzmze812NpJCHDjr486ZLulfi0ouEaQr0qVxPsyDpVqVI4gj1pssIpo2eiFWFXqlZoB09B6e3veHfHT_AEwPXt3DB4J6uqIzyI7nAGwouaKgemOkPSww3Qwnq4gg4uGiNBX_6PP4-49Is91xhhQ7YRSgZ__XjC0R2oIY4stJIq4WvHkeshoMI783LUJTJnPUXoWxkMn-JAVom6C9PgCFmP38hW63i5itM0TrNiXeTbNMIjsqTYLpN4s87SvMg2aZLkQ4Q_xgSFJEKSyhn7OCc-BT8pfkz78e3wC5gMfgQ?type=png)](https://mermaid.live/edit#pako:eNp1kE9Lw0AQxb_KMCetsSRNm6QLClKhXhTEPwfZy5Kd2IVkN252wRry3d0k7Umc0zDzmze812NpJCHDjr486ZLulfi0ouEaQr0qVxPsyDpVqVI4gj1pssIpo2eiFWFXqlZoB09B6e3veHfHT_AEwPXt3DB4J6uqIzyI7nAGwouaKgemOkPSww3Qwnq4gg4uGiNBX_6PP4-49Is91xhhQ7YRSgZ__XjC0R2oIY4stJIq4WvHkeshoMI783LUJTJnPUXoWxkMn-JAVom6C9PgCFmP38hW63i5itM0TrNiXeTbNMIjsqTYLpN4s87SvMg2aZLkQ4Q_xgSFJEKSyhn7OCc-BT8pfkz78e3wC5gMfgQ) 
The $Node_U$ will receive the previous output, and it will calculate its **private key** $d_u$ and its **public key** $Q_u$.