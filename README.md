# SEP10 WEB AUTHENTICATION TOKEN


[READ MORE DETAILS HERE](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0010.md#challenge)


* A basic Example 


```Python
from Authenticator.StellarAuthy import WebAuthy

webauth = WebAuthy(asset_code, asset_issuer, user_key) # This Also Accept _horizon_url and _network, _horizon_url is the horizon url, the default is the mainnet, _network can also be changed to tesnet default is mainnet
token = webauth.run_auth()

# JWT will be returned

```

[![Screenshot-2021-06-27-at-00-47-29.png](https://i.postimg.cc/3xRZ8rWQ/Screenshot-2021-06-27-at-00-47-29.png)](https://postimg.cc/TpzbQ6rt)