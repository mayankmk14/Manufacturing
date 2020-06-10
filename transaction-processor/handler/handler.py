import logging
import hashlib
import traceback

from sawtooth_sdk.processor.handler import TransactionHandler
import transaction_pb2 as tx_payload
from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.exceptions import InternalError
import handler.factory as Factory
import handler.register as Register_User
import handler.changeOwnership as Ownership
import handler.car as Car
import json
import os

current_dir=os.path.dirname(__file__)

LOGGER = logging.getLogger(__name__)

NAMESPACE = 'Car_Supply_Chain'
namespacePrefix = hashlib.sha512(NAMESPACE.encode('utf8')).hexdigest()[:6]

class Manufacturing(TransactionHandler):
    @property
    def family_name(self):
        return 'Car_Supply_Chain'

    @property
    def family_versions(self):
        return ['1.0']

    @property
    def namespaces(self):
        return [NAMESPACE]


    def apply(self, transaction, context):

            payloadobj=tx_payload.Payload()
            LOGGER.debug("TX ID-")
            LOGGER.error(transaction.signature)
            signer = transaction.header.signer_public_key
            LOGGER.debug("HANDLER")
            LOGGER.debug(payloadobj.action)
            payloadobj.ParseFromString(transaction.payload)
            LOGGER.debug(signer)
            
            actionSwitcher= {
                tx_payload.Payload.Action.ACCOUNT: Register_User.register_user,
                tx_payload.Payload.Action.CREATE_PARTS: Factory.create_order,
                tx_payload.Payload.Action.OWNERSHIP: Ownership.change_ownership,
                tx_payload.Payload.Action.CREATE_CAR: Car.create_car
            }

            if not (payloadobj.action in actionSwitcher):
                LOGGER.debug("no function invoked- "+payloadobj.action)
                raise InvalidTransaction("No action taken")

            LOGGER.debug('action'+str(payloadobj))
            command=actionSwitcher[payloadobj.action]
            try:
                command(payloadobj,signer,context,transaction.signature)
                LOGGER.debug("Done with function")
            except KeyboardInterrupt:
                pass
            except Exception as e:
                LOGGER.error(traceback.format_exc())
                raise InvalidTransaction(traceback.format_exc())