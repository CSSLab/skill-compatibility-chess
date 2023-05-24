# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_files.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_files.proto',
  package='maia',
  syntax='proto2',
  serialized_pb=_b('\n\x10\x64\x61ta_files.proto\x12\x04maia\"[\n\x07GameSet\x12\x11\n\tnum_games\x18\x01 \x01(\x07\x12\"\n\ngame_infos\x18\x02 \x03(\x0b\x32\x0e.maia.GameInfo\x12\x19\n\x05moves\x18\x03 \x03(\x0b\x32\n.maia.Move\"\xb8\x01\n\x08GameInfo\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x14\n\x0cwhite_player\x18\x02 \x01(\t\x12\x14\n\x0c\x62lack_player\x18\x03 \x01(\t\x12\x11\n\twhite_elo\x18\x04 \x01(\x07\x12\x11\n\tblack_elo\x18\x05 \x01(\x07\x12\x0f\n\x07num_ply\x18\x06 \x01(\x07\x12\x11\n\ttimestamp\x18\x07 \x01(\x07\x12\x12\n\nstart_time\x18\x08 \x01(\x07\x12\x11\n\tincrement\x18\t \x01(\x07\"\xac\x01\n\x04Move\x12\x10\n\x08is_white\x18\x01 \x01(\x08\x12\x12\n\nactive_won\x18\x02 \x01(\x08\x12\x11\n\tno_winner\x18\x03 \x01(\x08\x12\x10\n\x08move_ply\x18\x04 \x01(\x07\x12\r\n\x05\x62oard\x18\x05 \x01(\t\x12\x0c\n\x04move\x18\x06 \x01(\t\x12\x11\n\tmove_time\x18\x07 \x01(\x07\x12\x16\n\x0epre_move_clock\x18\x08 \x01(\x07\x12\x11\n\topp_clock\x18\t \x01(\x07')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GAMESET = _descriptor.Descriptor(
  name='GameSet',
  full_name='maia.GameSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_games', full_name='maia.GameSet.num_games', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_infos', full_name='maia.GameSet.game_infos', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moves', full_name='maia.GameSet.moves', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=117,
)


_GAMEINFO = _descriptor.Descriptor(
  name='GameInfo',
  full_name='maia.GameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='maia.GameInfo.game_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='white_player', full_name='maia.GameInfo.white_player', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='black_player', full_name='maia.GameInfo.black_player', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='white_elo', full_name='maia.GameInfo.white_elo', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='black_elo', full_name='maia.GameInfo.black_elo', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_ply', full_name='maia.GameInfo.num_ply', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='maia.GameInfo.timestamp', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='maia.GameInfo.start_time', index=7,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='increment', full_name='maia.GameInfo.increment', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=304,
)


_MOVE = _descriptor.Descriptor(
  name='Move',
  full_name='maia.Move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_white', full_name='maia.Move.is_white', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_won', full_name='maia.Move.active_won', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='no_winner', full_name='maia.Move.no_winner', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_ply', full_name='maia.Move.move_ply', index=3,
      number=4, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='board', full_name='maia.Move.board', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move', full_name='maia.Move.move', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_time', full_name='maia.Move.move_time', index=6,
      number=7, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_move_clock', full_name='maia.Move.pre_move_clock', index=7,
      number=8, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opp_clock', full_name='maia.Move.opp_clock', index=8,
      number=9, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=479,
)

_GAMESET.fields_by_name['game_infos'].message_type = _GAMEINFO
_GAMESET.fields_by_name['moves'].message_type = _MOVE
DESCRIPTOR.message_types_by_name['GameSet'] = _GAMESET
DESCRIPTOR.message_types_by_name['GameInfo'] = _GAMEINFO
DESCRIPTOR.message_types_by_name['Move'] = _MOVE

GameSet = _reflection.GeneratedProtocolMessageType('GameSet', (_message.Message,), dict(
  DESCRIPTOR = _GAMESET,
  __module__ = 'data_files_pb2'
  # @@protoc_insertion_point(class_scope:maia.GameSet)
  ))
_sym_db.RegisterMessage(GameSet)

GameInfo = _reflection.GeneratedProtocolMessageType('GameInfo', (_message.Message,), dict(
  DESCRIPTOR = _GAMEINFO,
  __module__ = 'data_files_pb2'
  # @@protoc_insertion_point(class_scope:maia.GameInfo)
  ))
_sym_db.RegisterMessage(GameInfo)

Move = _reflection.GeneratedProtocolMessageType('Move', (_message.Message,), dict(
  DESCRIPTOR = _MOVE,
  __module__ = 'data_files_pb2'
  # @@protoc_insertion_point(class_scope:maia.Move)
  ))
_sym_db.RegisterMessage(Move)


# @@protoc_insertion_point(module_scope)
