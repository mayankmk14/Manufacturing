import logging
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import assets_pb2 as assets

import json
import os
current_dir=os.path.dirname(__file__)
with open(os.path.join(current_dir, '../config.json')) as json_config:
    config = json.load(json_config)
LOGGER = logging.getLogger(__name__)


def check_admin_signer(signer):
    """ Checking whether signer is admin or not based on the public key
		
		Args:
			param1 (signer): public key of signer
        Returns:
            param1 (bool): True or False
    """
    if config["admin_signer_public_key"] != signer:
        return False
    return True

def store_Trail(orderId, txId, signer, assignedTo, signerOrgType, assetType):
    """ provide a serialized version of the provided arguments for setting Trail
		
		Args:
			param1 (orderId): assetId
            param2 (txId): Unique Id associated with each transaction used to track their status
            param3 (signer): Public key of transaction Signer(transactor)
            param4 (assignedTo): Owner organisation name after Transaction
            param5 (signerOrgType): Signer type
            param6 (assetType): asset type
		Returns:
            List : [
                (address): On-chain address to store Trail object for Order
                (serializedString) : Trail object
                    ]
    """
    LOGGER.debug("function Store Trail")
    thisTrail = assets.Trail()
    thisTrail.orderId = orderId
    thisTrail.txnNumber = txId
    thisTrail.signer = signer
    thisTrail.assignedTo = assignedTo
    thisTrail.signerOrgType = signerOrgType
    thisTrail.type = assetType
    address = Addressing.get_trail_address(orderId, signer, txId)
    thisTrail.address = address
    serializedString = thisTrail.SerializeToString()
    return [address,  serializedString]