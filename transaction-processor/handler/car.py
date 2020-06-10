import logging
import hashlib

import assets_pb2 as assets
from sawtooth_sdk.processor.exceptions import InvalidTransaction
import handler.addressing as Addressing
import handler.utils as utils

LOGGER = logging.getLogger(__name__)
def create_car(payloadobj,signer,context,txId):

    formDetails = payloadobj.car
    LOGGER.debug(formDetails)
    write_sets={}
    address = Addressing.get_user_address(signer)
    data_check=context.get_state([address])
    userAddress = Addressing.get_user_address(signer)
    engineAddress = Addressing.get_asset_address(formDetails.assetId, assets.AssetType.ENGINE)
    wheelAddress = Addressing.get_asset_address(formDetails.assetId, assets.AssetType.WHEEL)
    transmissionsAddress = Addressing.get_asset_address(formDetails.assetId, assets.AssetType.TRANSMISSIONS)
    data_check=context.get_state([userAddress, engineAddress, wheelAddress, transmissionsAddress])
    LOGGER.debug(len(data_check))
    if len(data_check) != 4:
        raise InvalidTransaction("One of the assets is not registered")
    else :
        LOGGER.info("All Assets found --- Lets create a car")

    # generate an address for car 
    assetAddress = Addressing.get_asset_address(formDetails.assetId, assets.AssetType.CAR)
    entries=context.get_state([userAddress, engineAddress, wheelAddress, transmissionsAddress])
    if len(entries) == 1:
        raise InvalidTransaction("Car Already Exists")
    else :
        LOGGER.info("Lets create a car")

    user_account = assets.Account()
    user_account.ParseFromString(data_check[0].data)
    LOGGER.info("Data loading Done - 1")
    if user_account.type != assets.OrgType.ORG_TYPE_CAR_FACTORY:
        raise InvalidTransaction("WRONG SIGNER TYPE")

    engine_asset = assets.FactoryAsset()
    engine_asset.ParseFromString(data_check[1].data)

    wheel_asset = assets.FactoryAsset()
    wheel_asset.ParseFromString(data_check[2].data)

    transmissions_asset = assets.FactoryAsset()
    transmissions_asset.ParseFromString(data_check[3].data)

    new_order = assets.Car()   
    new_order.address = assetAddress
    new_order.assetId = formDetails.assetId
    new_order.wheelId = wheel_asset.assetId
    new_order.engineId = engine_asset.assetId
    new_order.transmissionsId = transmissions_asset.assetId
    new_order.currentOwner = assets.OrgType.ORG_TYPE_CAR_FACTORY
    new_order.currentOwnerAddress = userAddress
    

    if(engine_asset.currentOwner == assets.OrgType.ORG_TYPE_PARTS_FACTORY):
        engine_asset.currentOwner = assets.OrgType.ORG_TYPE_CAR_FACTORY
        engine_asset.currentOwnerAddress = userAddress
        engine_asset.carAddress = assetAddress
        engine_trail = utils.store_Trail(engine_asset.assetId, txId, signer, user_account.organizationName, engine_asset.type)

    else :
        raise InvalidTransaction("=== Asset Already in use ===")

    if(wheel_asset.currentOwner == assets.OrgType.ORG_TYPE_PARTS_FACTORY):
        wheel_asset.currentOwner = assets.OrgType.ORG_TYPE_CAR_FACTORY
        wheel_asset.currentOwnerAddress = userAddress
        wheel_asset.carAddress = assetAddress
        wheel_trail = utils.store_Trail(wheel_asset.assetId, txId, signer, user_account.organizationName, wheel_asset.type)
        

    else :
        raise InvalidTransaction("=== Asset Already in use ===")

    if(transmissions_asset.currentOwner == assets.OrgType.ORG_TYPE_PARTS_FACTORY):
        transmissions_asset.currentOwner = assets.OrgType.ORG_TYPE_CAR_FACTORY
        transmissions_asset.currentOwnerAddress = userAddress
        transmissions_asset.carAddress = assetAddress
        transmissions_trail = utils.store_Trail(transmissions_trail.assetId, txId, signer, user_account.organizationName, transmissions_trail.type)

    else :
        raise InvalidTransaction("=== Asset Already in use ===")

    trail = utils.store_Trail(asset.assetId, txId, signer, user_account.organizationName, asset.type)
    write_sets[trail[0]] = trail[1]
    
    write_sets[userAddress]= user_account.SerializeToString()
    write_sets[assetAddress] = new_order.SerializeToString()
    write_sets[wheelAddress] = wheel_asset.SerializeToString()
    write_sets[engineAddress] = engine_asset.SerializeToString()
    write_sets[transmissionsAddress] = transmissions_asset.SerializeToString()
    write_sets[engine_trail[0]] = engine_trail[1]

    write_sets[wheel_trail[0]] = wheel_trail[1]
    write_sets[transmissions_trail[0]] = transmissions_trail[1]
    context.set_state(write_sets)