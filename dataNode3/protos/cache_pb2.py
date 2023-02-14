# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataNode3/protos/cache.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x64\x61taNode3/protos/cache.proto\x12\x05\x63\x61\x63he\"\x1b\n\x08segments\x12\x0f\n\x07segment\x18\x01 \x03(\t\"(\n\x0c\x44\x61taNodeSize\x12\x0c\n\x04size\x18\x01 \x01(\t\x12\n\n\x02IP\x18\x02 \x01(\t\"*\n\tmodelMeta\x12\x0c\n\x04name\x18\x01 \x03(\t\x12\x0f\n\x07segment\x18\x02 \x03(\t\"+\n\nwholeModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07segment\x18\x02 \x01(\t\"M\n\x0eObjectWithTime\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07segment\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\x0e\n\x06object\x18\x04 \x01(\x0c\"@\n\x11ModelInfoWithTime\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07segment\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\"7\n\x06object\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07segment\x18\x02 \x01(\t\x12\x0e\n\x06object\x18\x03 \x01(\x0c\"*\n\tmodelInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07segment\x18\x02 \x01(\t\"\x16\n\x08\x44\x61taNode\x12\n\n\x02\x44N\x18\x01 \x01(\t\"\x17\n\x05model\x12\x0e\n\x06object\x18\x01 \x01(\x0c\"\x17\n\x04text\x12\x0f\n\x07message\x18\x01 \x01(\t\"*\n\x0bserverSpecs\x12\n\n\x02\x44N\x18\x01 \x01(\t\x12\x0f\n\x07storage\x18\x02 \x01(\t\"\x17\n\x07\x62oolean\x12\x0c\n\x04\x62ool\x18\x01 \x01(\x08\x32\x8d\x02\n\x14getModelFromDataNode\x12*\n\x08getModel\x12\x10.cache.modelInfo\x1a\x0c.cache.model\x12+\n\x08putModel\x12\x11.cache.wholeModel\x1a\x0c.cache.model\x12\x37\n\x11putObjectWithTime\x12\x15.cache.ObjectWithTime\x1a\x0b.cache.text\x12\'\n\tputObject\x12\r.cache.object\x1a\x0b.cache.text\x12:\n\x10putModelWithTime\x12\x18.cache.ModelInfoWithTime\x1a\x0c.cache.model2o\n\x06\x65xtras\x12+\n\ninValidate\x12\x10.cache.modelInfo\x1a\x0b.cache.text\x12\x38\n\x17get_object_created_time\x12\x10.cache.modelInfo\x1a\x0b.cache.text2\xa7\x01\n\x0cttlInspector\x12,\n\x07inspect\x12\x0f.cache.segments\x1a\x10.cache.modelMeta\x12\x33\n\rserverStartUp\x12\x12.cache.serverSpecs\x1a\x0e.cache.boolean\x12\x34\n\x0eserverShutDown\x12\x12.cache.serverSpecs\x1a\x0e.cache.boolean2}\n\nupdateMeta\x12\x36\n\x12updateDataNodeMeta\x12\x13.cache.DataNodeSize\x1a\x0b.cache.text\x12\x37\n\x16updateEvictedModelMeta\x12\x10.cache.modelMeta\x1a\x0b.cache.textb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataNode3.protos.cache_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SEGMENTS._serialized_start=39
  _SEGMENTS._serialized_end=66
  _DATANODESIZE._serialized_start=68
  _DATANODESIZE._serialized_end=108
  _MODELMETA._serialized_start=110
  _MODELMETA._serialized_end=152
  _WHOLEMODEL._serialized_start=154
  _WHOLEMODEL._serialized_end=197
  _OBJECTWITHTIME._serialized_start=199
  _OBJECTWITHTIME._serialized_end=276
  _MODELINFOWITHTIME._serialized_start=278
  _MODELINFOWITHTIME._serialized_end=342
  _OBJECT._serialized_start=344
  _OBJECT._serialized_end=399
  _MODELINFO._serialized_start=401
  _MODELINFO._serialized_end=443
  _DATANODE._serialized_start=445
  _DATANODE._serialized_end=467
  _MODEL._serialized_start=469
  _MODEL._serialized_end=492
  _TEXT._serialized_start=494
  _TEXT._serialized_end=517
  _SERVERSPECS._serialized_start=519
  _SERVERSPECS._serialized_end=561
  _BOOLEAN._serialized_start=563
  _BOOLEAN._serialized_end=586
  _GETMODELFROMDATANODE._serialized_start=589
  _GETMODELFROMDATANODE._serialized_end=858
  _EXTRAS._serialized_start=860
  _EXTRAS._serialized_end=971
  _TTLINSPECTOR._serialized_start=974
  _TTLINSPECTOR._serialized_end=1141
  _UPDATEMETA._serialized_start=1143
  _UPDATEMETA._serialized_end=1268
# @@protoc_insertion_point(module_scope)
