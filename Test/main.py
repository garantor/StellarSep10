#Test for token returned
#Test for Error returned
# import sys
# sys.path.insert(0, "/home/afolabi/projects/StellarSep10/sep10")
# sys.path.insert(0, "/home/runner/work/StellarSep10/sep10")

from sep10 import Sep10
from pathlib import Path
client_key =  Path("/home/afolabi/projects/StellarSep10/.secrets").read_text()


import unittest


class Sep_10_Test(unittest.TestCase):
    
    def setUp(self) -> None:
        self.asset_code = "TZS"
        self.asset_issuer = "GA2MSSZKJOU6RNL3EJKH3S5TB5CDYTFQFWRYFGUJVIN5I6AOIRTLUHTO"
    
        return super().setUp()

    def test_case_1(self):
        asset_code = "TZS"
        asset_issuer = "GA2MSSZKJOU6RNL3EJKH3S5TB5CDYTFQFWRYFGUJVIN5I6AOIRTLUHTO"
        sep = Sep10(asset_code, asset_issuer, client_key)
        token = sep.run_auth()
        self.assertNotEquals(token, None)

    def test_case_2(self):
        #test for invalid asset_code
        asset_code = "THGSS"
        asset_issuer = "GA2MSSZKJOU6RNL3EJKH3S5TB5CDYTFQFWRYFGUJVIN5I6AOIRTLUHTO"
        sep = Sep10(asset_code, asset_issuer, client_key)
        token = sep.run_auth()
        self.assertEquals(token, None)

  


if __name__ == "__main__":
    unittest.main()