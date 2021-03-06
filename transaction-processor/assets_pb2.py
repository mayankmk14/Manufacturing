# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assets.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='assets.proto',
  package='Manufacturing',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x61ssets.proto\x12\rManufacturing\"\x93\x01\n\x07\x41\x63\x63ount\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x18\n\x10organizationName\x18\x02 \x01(\t\x12\r\n\x05orgId\x18\x03 \x01(\t\x12$\n\x04type\x18\x04 \x01(\x0e\x32\x16.Manufacturing.OrgType\x12\x11\n\tpublicKey\x18\x05 \x01(\t\x12\x15\n\raccountNumber\x18\x06 \x01(\t\"\xe6\x01\n\x0c\x46\x61\x63toryAsset\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12,\n\x0c\x63urrentOwner\x18\x02 \x01(\x0e\x32\x16.Manufacturing.OrgType\x12\x0f\n\x07\x61ssetId\x18\x03 \x01(\t\x12&\n\x04type\x18\x04 \x01(\x0e\x32\x18.Manufacturing.AssetType\x12\x16\n\x0e\x66\x61\x63toryAddress\x18\x05 \x01(\t\x12\x12\n\ncarAddress\x18\x06 \x01(\t\x12\x15\n\rdealerAddress\x18\x07 \x01(\t\x12\x1b\n\x13\x63urrentOwnerAddress\x18\x08 \x01(\t\"\xc5\x01\n\x03\x43\x61r\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12,\n\x0c\x63urrentOwner\x18\x02 \x01(\x0e\x32\x16.Manufacturing.OrgType\x12\x0f\n\x07\x61ssetId\x18\x03 \x01(\t\x12\x0f\n\x07wheelId\x18\x04 \x01(\t\x12\x10\n\x08\x65ngineId\x18\x05 \x01(\t\x12\x17\n\x0ftransmissionsId\x18\x06 \x01(\t\x12\x15\n\rdealerAddress\x18\x07 \x01(\t\x12\x1b\n\x13\x63urrentOwnerAddress\x18\x08 \x01(\t\"\xca\x01\n\x05Trail\x12\x0f\n\x07\x61ssetId\x18\x01 \x01(\t\x12\x11\n\ttxnNumber\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x0e\n\x06signer\x18\x04 \x01(\t\x12\x12\n\nassignedTo\x18\x05 \x01(\t\x12-\n\rsignerOrgType\x18\x06 \x01(\x0e\x32\x16.Manufacturing.OrgType\x12&\n\x04type\x18\x07 \x01(\x0e\x32\x18.Manufacturing.AssetType\x12\x0f\n\x07\x61\x64\x64ress\x18\x08 \x01(\t*@\n\tAssetType\x12\x08\n\x04VOID\x10\x00\x12\n\n\x06WHEELS\x10\x01\x12\n\n\x06\x45NGINE\x10\x02\x12\x11\n\rTRANSMISSIONS\x10\x03*g\n\x07OrgType\x12\x11\n\rORG_TYPE_VOID\x10\x00\x12\x1a\n\x16ORG_TYPE_PARTS_FACTORY\x10\x01\x12\x18\n\x14ORG_TYPE_CAR_FACTORY\x10\x02\x12\x13\n\x0fORG_TYPE_DEALER\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ASSETTYPE = _descriptor.EnumDescriptor(
  name='AssetType',
  full_name='Manufacturing.AssetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VOID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WHEELS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENGINE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSMISSIONS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=819,
  serialized_end=883,
)
_sym_db.RegisterEnumDescriptor(_ASSETTYPE)

AssetType = enum_type_wrapper.EnumTypeWrapper(_ASSETTYPE)
_ORGTYPE = _descriptor.EnumDescriptor(
  name='OrgType',
  full_name='Manufacturing.OrgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORG_TYPE_VOID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORG_TYPE_PARTS_FACTORY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORG_TYPE_CAR_FACTORY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORG_TYPE_DEALER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=885,
  serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_ORGTYPE)

OrgType = enum_type_wrapper.EnumTypeWrapper(_ORGTYPE)
VOID = 0
WHEELS = 1
ENGINE = 2
TRANSMISSIONS = 3
ORG_TYPE_VOID = 0
ORG_TYPE_PARTS_FACTORY = 1
ORG_TYPE_CAR_FACTORY = 2
ORG_TYPE_DEALER = 3



_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='Manufacturing.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='Manufacturing.Account.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='Manufacturing.Account.organizationName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orgId', full_name='Manufacturing.Account.orgId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Manufacturing.Account.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publicKey', full_name='Manufacturing.Account.publicKey', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accountNumber', full_name='Manufacturing.Account.accountNumber', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=179,
)


_FACTORYASSET = _descriptor.Descriptor(
  name='FactoryAsset',
  full_name='Manufacturing.FactoryAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='Manufacturing.FactoryAsset.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currentOwner', full_name='Manufacturing.FactoryAsset.currentOwner', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assetId', full_name='Manufacturing.FactoryAsset.assetId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Manufacturing.FactoryAsset.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factoryAddress', full_name='Manufacturing.FactoryAsset.factoryAddress', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carAddress', full_name='Manufacturing.FactoryAsset.carAddress', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dealerAddress', full_name='Manufacturing.FactoryAsset.dealerAddress', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currentOwnerAddress', full_name='Manufacturing.FactoryAsset.currentOwnerAddress', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=412,
)


_CAR = _descriptor.Descriptor(
  name='Car',
  full_name='Manufacturing.Car',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='Manufacturing.Car.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currentOwner', full_name='Manufacturing.Car.currentOwner', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assetId', full_name='Manufacturing.Car.assetId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheelId', full_name='Manufacturing.Car.wheelId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engineId', full_name='Manufacturing.Car.engineId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transmissionsId', full_name='Manufacturing.Car.transmissionsId', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dealerAddress', full_name='Manufacturing.Car.dealerAddress', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currentOwnerAddress', full_name='Manufacturing.Car.currentOwnerAddress', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=612,
)


_TRAIL = _descriptor.Descriptor(
  name='Trail',
  full_name='Manufacturing.Trail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='assetId', full_name='Manufacturing.Trail.assetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='txnNumber', full_name='Manufacturing.Trail.txnNumber', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Manufacturing.Trail.timestamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signer', full_name='Manufacturing.Trail.signer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignedTo', full_name='Manufacturing.Trail.assignedTo', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signerOrgType', full_name='Manufacturing.Trail.signerOrgType', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Manufacturing.Trail.type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='Manufacturing.Trail.address', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=615,
  serialized_end=817,
)

_ACCOUNT.fields_by_name['type'].enum_type = _ORGTYPE
_FACTORYASSET.fields_by_name['currentOwner'].enum_type = _ORGTYPE
_FACTORYASSET.fields_by_name['type'].enum_type = _ASSETTYPE
_CAR.fields_by_name['currentOwner'].enum_type = _ORGTYPE
_TRAIL.fields_by_name['signerOrgType'].enum_type = _ORGTYPE
_TRAIL.fields_by_name['type'].enum_type = _ASSETTYPE
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['FactoryAsset'] = _FACTORYASSET
DESCRIPTOR.message_types_by_name['Car'] = _CAR
DESCRIPTOR.message_types_by_name['Trail'] = _TRAIL
DESCRIPTOR.enum_types_by_name['AssetType'] = _ASSETTYPE
DESCRIPTOR.enum_types_by_name['OrgType'] = _ORGTYPE

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNT,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Manufacturing.Account)
  ))
_sym_db.RegisterMessage(Account)

FactoryAsset = _reflection.GeneratedProtocolMessageType('FactoryAsset', (_message.Message,), dict(
  DESCRIPTOR = _FACTORYASSET,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Manufacturing.FactoryAsset)
  ))
_sym_db.RegisterMessage(FactoryAsset)

Car = _reflection.GeneratedProtocolMessageType('Car', (_message.Message,), dict(
  DESCRIPTOR = _CAR,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Manufacturing.Car)
  ))
_sym_db.RegisterMessage(Car)

Trail = _reflection.GeneratedProtocolMessageType('Trail', (_message.Message,), dict(
  DESCRIPTOR = _TRAIL,
  __module__ = 'assets_pb2'
  # @@protoc_insertion_point(class_scope:Manufacturing.Trail)
  ))
_sym_db.RegisterMessage(Trail)


# @@protoc_insertion_point(module_scope)
