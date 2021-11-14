from sep10 import Sep10
from pathlib import Path
client_key =  Path("/home/afolabi/projects/StellarSep10/.secrets").read_text()


adc = Sep10("TZS", 'GA2MSSZKJOU6RNL3EJKH3S5TB5CDYTFQFWRYFGUJVIN5I6AOIRTLUHTO', client_key)
print(adc.run_auth())