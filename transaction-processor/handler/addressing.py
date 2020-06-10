import hashlib
import json
import os
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.constants as Constants
import assets_pb2 as assets

current_dir=os.path.dirname(__file__)

with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)

TF_ADDRESS_PREFIX = hashlib.sha512(config["FAMILY_NAME"].encode('utf-8')).hexdigest()[0:6]

assetPrefix={
    Constants.ASSET_TYPE_USER : hashlib.sha512(Constants.ASSET_TYPE_USER.encode('utf-8')).hexdigest()[0:6],
    Constants.ASSET_TYPE_TRAIL : hashlib.sha512(Constants.ASSET_TYPE_TRAIL.encode('utf-8')).hexdigest()[0:6],
    Constants.ASSET_TYPE_ID : hashlib.sha512(Constants.ASSET_TYPE_ID.encode('utf-8')).hexdigest()[0:6]
    
}

def get_user_address(signer):
    return TF_ADDRESS_PREFIX + assetPrefix[Constants.ASSET_TYPE_USER]+ hashlib.sha512(signer.encode('utf-8')).hexdigest()[0:58]


def get_trail_address(userName,userAddress,txId):
    return TF_ADDRESS_PREFIX + assetPrefix[Constants.ASSET_TYPE_TRAIL] + hashlib.sha512(userName.encode('utf-8')).hexdigest()[0:34] +  hashlib.sha512(userAddress.encode('utf-8')).hexdigest()[0:12] +  hashlib.sha512(txId.encode('utf-8')).hexdigest()[0:12]

def get_asset_address(assetId, asset_type):
    return TF_ADDRESS_PREFIX + assetPrefix[Constants.ASSET_TYPE_ID] + hashlib.sha512(assetId.encode('utf-8')).hexdigest()[0:34] +  hashlib.sha512(asset_type.encode('utf-8')).hexdigest()[0:24]
