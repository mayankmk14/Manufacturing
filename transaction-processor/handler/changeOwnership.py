import logging
import hashlib

import assets_pb2 as assets
import transaction_pb2 as tx
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

def change_ownership(payloadobj,signer,context,txId):
    """ Change OwnerShip of Factory assets
		
		Args:
			param1 (payloadObj): Payload associated with transaction
            param2 (signer): Public key of transaction Signer(transactor)
            param3 (context): stat context instance
            param4 (txId): Unique Id associated with each transaction used to track their status
		Returns:
    """
    LOGGER.info("Welcome to afInspect")
    write_sets = {}
    formDetails = payloadobj.changeOwnership
    LOGGER.debug(formDetails)

    userAddress = Addressing.get_user_address(signer)
    selectedUserAddress = Addressing.get_user_address(formDetails.newOwnerAddress )
    assetAddress = Addressing.get_asset_address(formDetails.assetId, formDetails.type)
    
    data_check=context.get_state([userAddress, selectedUserAddress, assetAddress])
    LOGGER.debug(len(data_check))

    if len(data_check) == 3:
        LOGGER.info("All Addresses Found")
    else :
        raise InvalidTransaction("Addresses not found")
    
    user_account = assets.Account()
    user_account.ParseFromString(data_check[0].data)
    LOGGER.info("Data loading Done - 1")
    
    selected_user_account = assets.Account()
    selected_user_account.ParseFromString(data_check[1].data)
    LOGGER.info("Data loading Done - 2")
    
    asset = assets.FactoryAsset()   
    asset.ParseFromString(data_check[2].data)
    LOGGER.info("Data loading Done - 3")
    
    if user_account.address == asset.currentOwnerAddress:
        LOGGER.info("Signer Doesn't Own the asset")
    else:
        raise InvalidTransaction("Wrong Signer for the asset")

    if selected_user_account.type == formDetails.assignToType:
        LOGGER.info("User Type Correct")
    else:
        raise InvalidTransaction("Wrong Assignee")
    
    # Change Ownership of CAR Asset
    if asset.type == assets.AssetType.CAR:
        if formDetails.assignToType == assets.OrgType.ORG_TYPE_DEALER:
            asset.dealerAddress = selected_user_account.address
        else :
            LOGGER.info("CAR ASSET CAN NOT BE ASSIGNED TO DEALERS")

        # Updating factory assets
        engineAddress = Addressing.get_asset_address(asset.engineId, assets.AssetType.ENGINE)
        wheelAddress = Addressing.get_asset_address(asset.wheelId, assets.AssetType.WHEEL)
        transmissionsAddress = Addressing.get_asset_address(asset.transmissionsId, assets.AssetType.TRANSMISSIONS)
        entries=context.get_state([engineAddress, wheelAddress, transmissionsAddress])
        if len(entries) == 3:
            LOGGER.info("All Addresses Found")
        else :
            raise InvalidTransaction("Addresses not found")

        engine_asset.currentOwner = assets.OrgType.ORG_TYPE_DEALER
        engine_asset.currentOwnerAddress = selectedUserAddress
        engine_asset.dealerAddress = selectedUserAddress
        engine_trail = utils.store_Trail(engine_asset.assetId, txId, signer, selected_user_account.organizationName, engine_asset.type)


        wheel_asset.currentOwner = assets.OrgType.ORG_TYPE_DEALER
        wheel_asset.currentOwnerAddress = selectedUserAddress
        wheel_asset.dealerAddress = selectedUserAddress
        wheel_trail = utils.store_Trail(wheel_asset.assetId, txId, signer, selected_user_account.organizationName, wheel_asset.type)
        
        transmissions_asset.currentOwner = assets.OrgType.ORG_TYPE_DEALER
        transmissions_asset.currentOwnerAddress = selectedUserAddress
        transmissions_asset.dealerAddress = selectedUserAddress
        transmissions_trail = utils.store_Trail(transmissions_asset.assetId, txId, signer, selected_user_account.organizationName, transmissions_asset.type)
        
    else :
    # Change ownership of Factory assets 
        if formDetails.assignToType == assets.OrgType.ORG_TYPE_CAR_FACTORY:
            asset.carAddress = selected_user_account.address
        elif formDetails.assignToType == assets.OrgType.ORG_TYPE_DEALER:
            asset.dealerAddress = selected_user_account.address
        else :
            LOGGER.info("FACTORY ASSET CAN NOT BE ASSIGNED TO OTHER FACTORY")

    asset.currentOwner = selected_user_account.type
    asset.currentOwnerAddress = selected_user_account.address
    trail = utils.store_Trail(asset.assetId, txId, signer, selected_user_account.organizationName, asset.type)
    write_sets[trail[0]] = trail[1]
    write_sets[engine_trail[0]] = engine_trail[1]
    write_sets[wheel_trail[0]] = wheel_trail[1]
    write_sets[transmissions_trail[0]] = transmissions_trail[1]
    write_sets[assetAddress] = asset.SerializeToString()
    LOGGER.info("Setting Context for States")
    LOGGER.debug(write_sets)
    context.set_state(write_sets)