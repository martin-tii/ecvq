
### 3. Mutual Authentication  
  
Nodes $U$ and $V$ generate a new nonce ($N$) to include freshness in the message. Node $U$ will send ($U$,$V$,$N_u$) along  with hash of the $H$($U$,$V$,$N_u$) for authentication. Node $V$, will compare the hash by computing hash of ($U$,$V$,$N_u$), with the secret key  generated at its side ($k_{vu}$). Node V, will send ($V$, $U$,$N_v$), concatenated with the hash of the $H$($V$, $U$,$N_v$), for authentication. Node $U$, will verify the hash by comparing the hash with the help of secret key generated at its side ($k_{uv}$).

**Input:**

1. The elliptic curve domain parameters established by CA  
2. shared secret key $k_{uv}$,$k_{vu}$ 
3. Identity of other node $V$

[![](https://mermaid.ink/img/pako:eNqNkTFrwzAQhf-KuKkFNcRW7cYaAoUOgZAsrTy07qDal0Rgy64ihaYh_72q5SRQMvSG43i6Tw_uHaBsKwQOW_x0qEt8UnJtZFNo4utF2RrJwlkna_Lo7Aa1VaW0qtVhoZPGC6qT2pKl_0hcl_MgGywtMeuPmyiLKIlj5luS3IbHHid302kgOBE0p0tBZ2_DMHe797CKurowuWdOSI5GrdSezOR280_L_GwpPE8FXebechjmO3fNUpwsxV9LoNCgaaSq_EkPv0QB_moNFsD9WOFKutoWUOijX5XOts97XQJfyXqLFFxXSXuK4Kz6MwI_wBdwNk5HLE0mydBSCnvgGRvdZ0nGhpYeKXy3reej0TgUm8SThyzOGAWslG3NIoTeZ98bvPaANQ6PP65fn60?type=png)](https://mermaid.live/edit#pako:eNqNkTFrwzAQhf-KuKkFNcRW7cYaAoUOgZAsrTy07qDal0Rgy64ihaYh_72q5SRQMvSG43i6Tw_uHaBsKwQOW_x0qEt8UnJtZFNo4utF2RrJwlkna_Lo7Aa1VaW0qtVhoZPGC6qT2pKl_0hcl_MgGywtMeuPmyiLKIlj5luS3IbHHid302kgOBE0p0tBZ2_DMHe797CKurowuWdOSI5GrdSezOR280_L_GwpPE8FXebechjmO3fNUpwsxV9LoNCgaaSq_EkPv0QB_moNFsD9WOFKutoWUOijX5XOts97XQJfyXqLFFxXSXuK4Kz6MwI_wBdwNk5HLE0mydBSCnvgGRvdZ0nGhpYeKXy3reej0TgUm8SThyzOGAWslG3NIoTeZ98bvPaANQ6PP65fn60)

**Output:**

Authentication
