# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_frame.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import handle_pb2 as handle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61udio_frame.proto\x12\rlivekit.proto\x1a\x0chandle.proto\"a\n\x17\x41llocAudioBufferRequest\x12\x13\n\x0bsample_rate\x18\x01 \x01(\r\x12\x14\n\x0cnum_channels\x18\x02 \x01(\r\x12\x1b\n\x13samples_per_channel\x18\x03 \x01(\r\"O\n\x18\x41llocAudioBufferResponse\x12\x33\n\x06\x62uffer\x18\x01 \x01(\x0b\x32#.livekit.proto.AudioFrameBufferInfo\"w\n\x15NewAudioStreamRequest\x12\x30\n\x0ctrack_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.AudioStreamType\"H\n\x16NewAudioStreamResponse\x12.\n\x06stream\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.AudioStreamInfo\"\x8a\x01\n\x15NewAudioSourceRequest\x12,\n\x04type\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.AudioSourceType\x12\x37\n\x07options\x18\x02 \x01(\x0b\x32!.livekit.proto.AudioSourceOptionsH\x00\x88\x01\x01\x42\n\n\x08_options\"H\n\x16NewAudioSourceResponse\x12.\n\x06source\x18\x01 \x01(\x0b\x32\x1e.livekit.proto.AudioSourceInfo\"\x80\x01\n\x18\x43\x61ptureAudioFrameRequest\x12\x31\n\rsource_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x31\n\rbuffer_handle\x18\x02 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\"\x1b\n\x19\x43\x61ptureAudioFrameResponse\"\x1a\n\x18NewAudioResamplerRequest\"G\n\x19NewAudioResamplerResponse\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\"\xad\x01\n\x17RemixAndResampleRequest\x12\x34\n\x10resampler_handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x31\n\rbuffer_handle\x18\x02 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x14\n\x0cnum_channels\x18\x03 \x01(\r\x12\x13\n\x0bsample_rate\x18\x04 \x01(\r\"O\n\x18RemixAndResampleResponse\x12\x33\n\x06\x62uffer\x18\x01 \x01(\x0b\x32#.livekit.proto.AudioFrameBufferInfo\"\x9c\x01\n\x14\x41udioFrameBufferInfo\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x14\n\x0cnum_channels\x18\x03 \x01(\r\x12\x13\n\x0bsample_rate\x18\x04 \x01(\r\x12\x1b\n\x13samples_per_channel\x18\x05 \x01(\r\"k\n\x0f\x41udioStreamInfo\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.AudioStreamType\"\x86\x01\n\x10\x41udioStreamEvent\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12;\n\x0e\x66rame_received\x18\x02 \x01(\x0b\x32!.livekit.proto.AudioFrameReceivedH\x00\x42\t\n\x07message\"H\n\x12\x41udioFrameReceived\x12\x32\n\x05\x66rame\x18\x01 \x01(\x0b\x32#.livekit.proto.AudioFrameBufferInfo\"e\n\x12\x41udioSourceOptions\x12\x19\n\x11\x65\x63ho_cancellation\x18\x01 \x01(\x08\x12\x19\n\x11noise_suppression\x18\x02 \x01(\x08\x12\x19\n\x11\x61uto_gain_control\x18\x03 \x01(\x08\"k\n\x0f\x41udioSourceInfo\x12*\n\x06handle\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.FfiHandleId\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.AudioSourceType*A\n\x0f\x41udioStreamType\x12\x17\n\x13\x41UDIO_STREAM_NATIVE\x10\x00\x12\x15\n\x11\x41UDIO_STREAM_HTML\x10\x01**\n\x0f\x41udioSourceType\x12\x17\n\x13\x41UDIO_SOURCE_NATIVE\x10\x00\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_frame_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_AUDIOSTREAMTYPE']._serialized_start=1849
  _globals['_AUDIOSTREAMTYPE']._serialized_end=1914
  _globals['_AUDIOSOURCETYPE']._serialized_start=1916
  _globals['_AUDIOSOURCETYPE']._serialized_end=1958
  _globals['_ALLOCAUDIOBUFFERREQUEST']._serialized_start=50
  _globals['_ALLOCAUDIOBUFFERREQUEST']._serialized_end=147
  _globals['_ALLOCAUDIOBUFFERRESPONSE']._serialized_start=149
  _globals['_ALLOCAUDIOBUFFERRESPONSE']._serialized_end=228
  _globals['_NEWAUDIOSTREAMREQUEST']._serialized_start=230
  _globals['_NEWAUDIOSTREAMREQUEST']._serialized_end=349
  _globals['_NEWAUDIOSTREAMRESPONSE']._serialized_start=351
  _globals['_NEWAUDIOSTREAMRESPONSE']._serialized_end=423
  _globals['_NEWAUDIOSOURCEREQUEST']._serialized_start=426
  _globals['_NEWAUDIOSOURCEREQUEST']._serialized_end=564
  _globals['_NEWAUDIOSOURCERESPONSE']._serialized_start=566
  _globals['_NEWAUDIOSOURCERESPONSE']._serialized_end=638
  _globals['_CAPTUREAUDIOFRAMEREQUEST']._serialized_start=641
  _globals['_CAPTUREAUDIOFRAMEREQUEST']._serialized_end=769
  _globals['_CAPTUREAUDIOFRAMERESPONSE']._serialized_start=771
  _globals['_CAPTUREAUDIOFRAMERESPONSE']._serialized_end=798
  _globals['_NEWAUDIORESAMPLERREQUEST']._serialized_start=800
  _globals['_NEWAUDIORESAMPLERREQUEST']._serialized_end=826
  _globals['_NEWAUDIORESAMPLERRESPONSE']._serialized_start=828
  _globals['_NEWAUDIORESAMPLERRESPONSE']._serialized_end=899
  _globals['_REMIXANDRESAMPLEREQUEST']._serialized_start=902
  _globals['_REMIXANDRESAMPLEREQUEST']._serialized_end=1075
  _globals['_REMIXANDRESAMPLERESPONSE']._serialized_start=1077
  _globals['_REMIXANDRESAMPLERESPONSE']._serialized_end=1156
  _globals['_AUDIOFRAMEBUFFERINFO']._serialized_start=1159
  _globals['_AUDIOFRAMEBUFFERINFO']._serialized_end=1315
  _globals['_AUDIOSTREAMINFO']._serialized_start=1317
  _globals['_AUDIOSTREAMINFO']._serialized_end=1424
  _globals['_AUDIOSTREAMEVENT']._serialized_start=1427
  _globals['_AUDIOSTREAMEVENT']._serialized_end=1561
  _globals['_AUDIOFRAMERECEIVED']._serialized_start=1563
  _globals['_AUDIOFRAMERECEIVED']._serialized_end=1635
  _globals['_AUDIOSOURCEOPTIONS']._serialized_start=1637
  _globals['_AUDIOSOURCEOPTIONS']._serialized_end=1738
  _globals['_AUDIOSOURCEINFO']._serialized_start=1740
  _globals['_AUDIOSOURCEINFO']._serialized_end=1847
# @@protoc_insertion_point(module_scope)
