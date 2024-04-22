# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: riva/proto/riva_tts.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import riva_audio_pb2 as riva_dot_proto_dot_riva__audio__pb2
from . import riva_common_pb2 as riva_dot_proto_dot_riva__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19riva/proto/riva_tts.proto\x12\x0fnvidia.riva.tts\x1a\x1briva/proto/riva_audio.proto\x1a\x1criva/proto/riva_common.proto\"0\n\x1aRivaSynthesisConfigRequest\x12\x12\n\nmodel_name\x18\x01 \x01(\t\"\x93\x02\n\x1bRivaSynthesisConfigResponse\x12I\n\x0cmodel_config\x18\x01 \x03(\x0b\x32\x33.nvidia.riva.tts.RivaSynthesisConfigResponse.Config\x1a\xa8\x01\n\x06\x43onfig\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12W\n\nparameters\x18\x02 \x03(\x0b\x32\x43.nvidia.riva.tts.RivaSynthesisConfigResponse.Config.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"{\n\x0cZeroShotData\x12\x14\n\x0c\x61udio_prompt\x18\x01 \x01(\x0c\x12\x16\n\x0esample_rate_hz\x18\x02 \x01(\x05\x12,\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x1a.nvidia.riva.AudioEncoding\x12\x0f\n\x07quality\x18\x04 \x01(\x05\"\xf3\x01\n\x17SynthesizeSpeechRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12,\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x1a.nvidia.riva.AudioEncoding\x12\x16\n\x0esample_rate_hz\x18\x04 \x01(\x05\x12\x12\n\nvoice_name\x18\x05 \x01(\t\x12\x35\n\x0ezero_shot_data\x18\x06 \x01(\x0b\x32\x1d.nvidia.riva.tts.ZeroShotData\x12\"\n\x02id\x18\x64 \x01(\x0b\x32\x16.nvidia.riva.RequestId\"e\n SynthesizeSpeechResponseMetadata\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x16\n\x0eprocessed_text\x18\x02 \x01(\t\x12\x1b\n\x13predicted_durations\x18\x08 \x03(\x02\"\x8e\x01\n\x18SynthesizeSpeechResponse\x12\r\n\x05\x61udio\x18\x01 \x01(\x0c\x12?\n\x04meta\x18\x02 \x01(\x0b\x32\x31.nvidia.riva.tts.SynthesizeSpeechResponseMetadata\x12\"\n\x02id\x18\x64 \x01(\x0b\x32\x16.nvidia.riva.RequestId2\xde\x02\n\x13RivaSpeechSynthesis\x12\x63\n\nSynthesize\x12(.nvidia.riva.tts.SynthesizeSpeechRequest\x1a).nvidia.riva.tts.SynthesizeSpeechResponse\"\x00\x12k\n\x10SynthesizeOnline\x12(.nvidia.riva.tts.SynthesizeSpeechRequest\x1a).nvidia.riva.tts.SynthesizeSpeechResponse\"\x00\x30\x01\x12u\n\x16GetRivaSynthesisConfig\x12+.nvidia.riva.tts.RivaSynthesisConfigRequest\x1a,.nvidia.riva.tts.RivaSynthesisConfigResponse\"\x00\x42\x1bZ\x16nvidia.com/riva_speech\xf8\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'riva.proto.riva_tts_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\026nvidia.com/riva_speech\370\001\001'
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG_PARAMETERSENTRY']._options = None
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_RIVASYNTHESISCONFIGREQUEST']._serialized_start=105
  _globals['_RIVASYNTHESISCONFIGREQUEST']._serialized_end=153
  _globals['_RIVASYNTHESISCONFIGRESPONSE']._serialized_start=156
  _globals['_RIVASYNTHESISCONFIGRESPONSE']._serialized_end=431
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG']._serialized_start=263
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG']._serialized_end=431
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG_PARAMETERSENTRY']._serialized_start=382
  _globals['_RIVASYNTHESISCONFIGRESPONSE_CONFIG_PARAMETERSENTRY']._serialized_end=431
  _globals['_ZEROSHOTDATA']._serialized_start=433
  _globals['_ZEROSHOTDATA']._serialized_end=556
  _globals['_SYNTHESIZESPEECHREQUEST']._serialized_start=559
  _globals['_SYNTHESIZESPEECHREQUEST']._serialized_end=802
  _globals['_SYNTHESIZESPEECHRESPONSEMETADATA']._serialized_start=804
  _globals['_SYNTHESIZESPEECHRESPONSEMETADATA']._serialized_end=905
  _globals['_SYNTHESIZESPEECHRESPONSE']._serialized_start=908
  _globals['_SYNTHESIZESPEECHRESPONSE']._serialized_end=1050
  _globals['_RIVASPEECHSYNTHESIS']._serialized_start=1053
  _globals['_RIVASPEECHSYNTHESIS']._serialized_end=1403
# @@protoc_insertion_point(module_scope)