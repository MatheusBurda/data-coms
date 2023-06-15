import rsa
from rsa import PrivateKey, PublicKey
import base64
# publicKey, privateKey = rsa.newkeys(512)
 
public_key = PublicKey(7230269301988559979337639455381003704586452965567203023471175639098818841749304457976763561206166007829276289137742445594066590789737588351804345394692213, 65537)
private_key = PrivateKey(7230269301988559979337639455381003704586452965567203023471175639098818841749304457976763561206166007829276289137742445594066590789737588351804345394692213, 65537, 620569522921184214775992522338803207932905044956521003509854936447058241110476409122376697412121723395420527368516049864620728732940417695673552552360973, 6610230248055727800149195711919748835776506380824589348963857849564032960362975723, 1093799917803953160591185212978936267440117473119974644650641142609657631)

def encrypt(message):
    encMessage_bytes = rsa.encrypt(message.encode(), public_key)
    return base64.b64encode(encMessage_bytes).decode('ascii')


def decrypt(b64_str):
    encMessage_from_base_64 =  base64.b64decode(b64_str.encode('ascii'))
    return rsa.decrypt(encMessage_from_base_64, private_key).decode()
