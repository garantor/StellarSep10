# SEP10 WEB AUTHENTICATION TOKEN

For A Full Understanding of Sep10, Please visit the official repo [READ MORE DETAILS HERE](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0010.md#challenge).




After clone or fork this repo, then 

```Python
pip install sep10
```
After installation, it's ready for use, Below is a basic Example of how to use the repo


```Python
from Authenticator.StellarAuthy import WebAuthy

webauth = WebAuthy(asset_code, asset_issuer, user_key) # This Also Accept _horizon_url and _network, _horizon_url is the horizon url, the default is the mainnet, _network can also be changed to tesnet default is mainnet
token = webauth.run_auth()

# JWT will be returned

```


[![Screenshot-2021-06-27-at-11-21-19.png](https://i.postimg.cc/fWFVFckz/Screenshot-2021-06-27-at-11-21-19.png)](https://postimg.cc/0rY5KJpF)