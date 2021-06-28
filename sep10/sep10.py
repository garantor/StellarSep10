from flask.globals import request
import requests, json, toml, validators
from stellar_sdk.server import Server
from stellar_sdk.network import Network
from stellar_sdk.transaction_envelope import TransactionEnvelope
from stellar_sdk.sep.exceptions import InvalidSep10ChallengeError
from stellar_sdk.keypair import Keypair


# general_server = Server(horizon_url="https://horizon.stellar.org")
# domain = "https://sentit.io/"


class Sep10:
    def __init__(self, asset_code, asset_issuer, user_key, _horizon_url="https://horizon.stellar.org", _network=Network.PUBLIC_NETWORK_PASSPHRASE):
        """
        Instantial the webauthy by passing in the following args

        asset_code: The Asset code
        asset_issuer: Token Asset issuer
        user_key: The secret key to sign chanllenge transaction(user private key)
        _horizon_url: Default is set to mainnet and is optional
        _network: Default is set to mainnet and is optional
        """
        
        self.asset_code = asset_code
        self.asset_issuer = asset_issuer
        self.pub_key = Keypair.from_secret(user_key).public_key
        self.user_signing_key =  user_key
        self.general_stellar_url = _horizon_url
        self.NETWORK_PASSPHRASE = _network
        self.server = Server(horizon_url=self.general_stellar_url)
        # self.run_auth()
    def run_auth(self):
        url_ = f"{self.general_stellar_url}/assets?asset_code={self.asset_code}&asset_issuer={self.asset_issuer}"
        resquest = requests.get(url=url_)


        sep_10_token = None
      

        if resquest.status_code == 200:
            token = self.sep10_successful_request(resquest.content.decode())
            return token
        if resquest.status_code != 200:
            error_getting_token = self.sep10_failed_requests(resquest.content.decode())
            return error_getting_token

    
    def sep10_successful_request(self, web_content):
        web_content = json.loads(web_content)
        toml_url =web_content['_embedded']['records'][0]['_links']['toml']['href'] 
        url_validate = validators.url(toml_url)
        if url_validate == True:
            transfer_serve = requests.get(toml_url)
            server_res =transfer_serve.content.decode()
            try:
                global toml_content
                toml_content = toml.loads(server_res)
            except toml.decoder.TomlDecodeError:
                return {"error": 'Error Loading Toml file'}, 403


            else:
                
                try:

                    WEB_AUTH_ENDPOINT = toml_content['WEB_AUTH_ENDPOINT']
                except Exception as e:
                    return {"error": 'Error Loading Toml file'}, 400


                else:
                    
                    WEB_AUTH_URL= f"{WEB_AUTH_ENDPOINT}/?account={self.pub_key}"

                    headers = {
                    "Content-type": "application/json",
                    # "Accept": "text/plain",
                    }
                    getting_challeng_key = requests.get(WEB_AUTH_URL)
                    if getting_challeng_key.status_code == 200:
                        sep_token = self.sign_sep10_tx(getting_challeng_key.json())
                        return sep_token

                    else:
                        self.sep10_failed_requests()

                

        else:
            return {"error": 'Invalide Url'}, 400

    def sign_sep10_tx(self, tx_web_content):
        WEB_AUTH_ENDPOINT = toml_content['WEB_AUTH_ENDPOINT']
            
        server_signing_key = toml_content['SIGNING_KEY']
        
        challeng_transaction = tx_web_content
        envelope_xdr = challeng_transaction['transaction']
        envelope_object = TransactionEnvelope.from_xdr(
            envelope_xdr, network_passphrase=self.NETWORK_PASSPHRASE
        )
        transaction = envelope_object.transaction

# verify that transaction source account is equal to the server's signing key
        if transaction.source.public_key != server_signing_key:
            raise InvalidSep10ChallengeError(
                "Transaction source account is not equal to server's account."
            )

        # verify that transaction sequenceNumber is equal to zero
        elif transaction.sequence != 0:
            raise InvalidSep10ChallengeError(
                "The transaction sequence number should be zero."
            )

        else:
            #we need to get user signing key

            client_signing_key = self.user_signing_key
            envelope_object.sign(client_signing_key)
            client_signed_envelope_xdr = envelope_object.to_xdr()
            response = requests.post(
            WEB_AUTH_ENDPOINT,
            json={"transaction": client_signed_envelope_xdr},
                    )
            content = json.loads(response.content)

            sep10_token = content['token']

            return sep10_token

    def sep10_failed_requests(self, req_content):
        return {"error": 'Invalide Url'}, 400