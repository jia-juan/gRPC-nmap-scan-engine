# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scan.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nscan.proto\"\xc3\x01\n\rScanParameter\x12\x10\n\x08scan_mod\x18\x01 \x01(\t\x12\x17\n\x0fscan_host_range\x18\x02 \x01(\t\x12\x16\n\x0escan_host_port\x18\x03 \x01(\t\x12\x19\n\x11scan_host_exclude\x18\x04 \x01(\t\x12\x12\n\nscan_speed\x18\x05 \x01(\t\x12\x12\n\nscan_delay\x18\x06 \x01(\t\x12\x19\n\x11scan_host_timeout\x18\x07 \x01(\t\x12\x11\n\tscan_args\x18\x08 \x01(\t\"-\n\nScanResult\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x13\n\x0bscan_result\x18\x02 \x01(\t26\n\x0bScanService\x12\'\n\x04Scan\x12\x0e.ScanParameter\x1a\x0b.ScanResult\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scan_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCANPARAMETER._serialized_start=15
  _SCANPARAMETER._serialized_end=210
  _SCANRESULT._serialized_start=212
  _SCANRESULT._serialized_end=257
  _SCANSERVICE._serialized_start=259
  _SCANSERVICE._serialized_end=313
# @@protoc_insertion_point(module_scope)
