import logging
import hashlib

import transaction_pb2 as tx
import assets_pb2 as assets
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import handler.constants as constants
import handler.utils as utils

import json
import os
current_dir=os.path.dirname(__file__)
with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)
LOGGER = logging.getLogger(__name__)

def create_order(payloadobj,signer,context,txId):
    """ Factory Part Creation on Blockchain
		
		Args:
			param1 (payloadObj): Payload associated with transaction
            param2 (signer): Public key of transaction Signer(transactor)
            param3 (context): stat context instance
            param4 (txId): Unique Id associated with each transaction used to track their status
		Returns:
    """
    LOGGER.info("Create Part - Factory")
    write_sets={}
    formDetails = payloadobj.factoryAsset
    LOGGER.debug(formDetails)
    factoryAddress = Addressing.get_user_address(signer)
    data_check=context.get_state([factoryAddress])
    LOGGER.info("States Read")
    LOGGER.debug(len(data_check))
    if len(data_check)== 0:
        raise InvalidTransaction("Factory Doesn't Exist")
    account = assets.Account()
    account.ParseFromString(data_check[0].data)
    LOGGER.info("Signer Type FACTORY === Confirming")
    LOGGER.debug(account.type)
    if account.type != assets.OrgType.ORG_TYPE_PARTS_FACTORY:
        raise InvalidTransaction("WRONG SIGNER TYPE")
    assetAddress = Addressing.get_asset_address(formDetails.assetId, formDetails.type)
    LOGGER.debug(assetAddress)
    new_order = assets.FactoryAsset()   
    new_order.address = assetAddress
    new_order.assetId = formDetails.assetId
    new_order.type = formDetails.type
    new_order.currentOwner = account.type
    new_order.factoryAddress = account.address


    parts_trail = utils.store_Trail(formDetails.assetId,txId, signer, account.organizationName, account.OrgType, new_order.type)
    write_sets[parts_trail[0]] = parts_trail[1]
    write_sets[assetAddress] = new_order.SerializeToString()
    LOGGER.info("Setting Context for States")
    LOGGER.debug(write_sets)
    context.set_state(write_sets)