import logging
import hashlib

import assets_pb2 as assets
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing

import json
import os
current_dir=os.path.dirname(__file__)
with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)
LOGGER = logging.getLogger(__name__)

def register_user(payloadobj,signer,context,txId):
    """ Registering User On Blockchain - With its PublicKey and Type
		
		Args:
			param1 (payloadObj): Payload associated with transaction
            param2 (signer): Public key of transaction Signer(transactor)
            param3 (context): stat context instance
            param4 (txId): Unique Id associated with each transaction used to track their status
		Returns:
    """
    user_details=payloadobj.userEnrollment
    LOGGER.debug("IN register_user")
    LOGGER.debug(user_details)
    is_admin=utils.check_admin_signer(signer)
    LOGGER.info("Verify Signer")
    if not is_admin:
        raise InvalidTransaction("Signer Not Admin")
    if(not user_details.publicKey or not user_details.type or not user_details.accountNumber or not user_details.organizationName ) :
        raise InvalidTransaction("Wrong Input")
    length_pub = len(user_details.publicKey)
    LOGGER.debug(length_pub)
    if (length_pub != 66):
        raise InvalidTransaction("Wrong Public Length Key")
    LOGGER.info("Verify Public Key")
    userAddress = Addressing.get_user_address(user_details.publicKey)
    user_check=context.get_state([userAddress])
    if len(user_check)!= 0:
        raise InvalidTransaction("Public Already Used")
    write_sets={}
    new_account=assets.Account()
    new_account.address= userAddress
    new_account.organizationName=user_details.organizationName
    new_account.accountNumber=user_details.accountNumber
    new_account.type=user_details.type
    new_account.publicKey=user_details.publicKey
    LOGGER.info("Account Field Updated")
    LOGGER.debug(new_account)
    write_sets[userAddress]=new_account.SerializeToString()
    LOGGER.info("Setting Context for States")
    LOGGER.debug(write_sets)
    context.set_state(write_sets)