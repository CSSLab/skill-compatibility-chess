# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chunk.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .net_pb2 import _ENGINEVERSION as net__pb2_ENGINEVERSION
from .net_pb2 import DESCRIPTOR as net__pb2_DESCRIPTOR

DESCRIPTOR = _descriptor.FileDescriptor(
    name="chunk.proto",
    package="pblczero",
    syntax="proto2",
    serialized_pb=_b(
        '\n\x0b\x63hunk.proto\x12\x08pblczero\x1a\tnet.proto"\x83\x01\n\x05State\x12\x11\n\x05plane\x18\x01 \x03(\x06\x42\x02\x10\x01\x12\x0e\n\x06us_ooo\x18\x02 \x01(\r\x12\r\n\x05us_oo\x18\x03 \x01(\r\x12\x10\n\x08them_ooo\x18\x04 \x01(\r\x12\x0f\n\x07them_oo\x18\x05 \x01(\r\x12\x14\n\x0cside_to_move\x18\x06 \x01(\r\x12\x0f\n\x07rule_50\x18\x07 \x01(\r".\n\x06Policy\x12\x11\n\x05index\x18\x01 \x03(\rB\x02\x10\x01\x12\x11\n\x05prior\x18\x02 \x03(\x02\x42\x02\x10\x01"\xbe\x01\n\x04Game\x12\x1e\n\x05state\x18\x01 \x03(\x0b\x32\x0f.pblczero.State\x12 \n\x06policy\x18\x02 \x03(\x0b\x32\x10.pblczero.Policy\x12\x11\n\x05value\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x10\n\x04move\x18\x04 \x03(\rB\x02\x10\x01\x12%\n\x06result\x18\x05 \x01(\x0e\x32\x15.pblczero.Game.Result"(\n\x06Result\x12\t\n\x05WHITE\x10\x00\x12\t\n\x05\x42LACK\x10\x01\x12\x08\n\x04\x44RAW\x10\x02"o\n\x05\x43hunk\x12\r\n\x05magic\x18\x01 \x01(\x07\x12\x0f\n\x07license\x18\x02 \x01(\t\x12(\n\x07version\x18\x03 \x01(\x0b\x32\x17.pblczero.EngineVersion\x12\x1c\n\x04game\x18\x04 \x03(\x0b\x32\x0e.pblczero.Game'
    ),
    dependencies=[
        net__pb2_DESCRIPTOR,
    ],
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_GAME_RESULT = _descriptor.EnumDescriptor(
    name="Result",
    full_name="pblczero.Game.Result",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="WHITE", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BLACK", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DRAW", index=2, number=2, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=369,
    serialized_end=409,
)
_sym_db.RegisterEnumDescriptor(_GAME_RESULT)


_STATE = _descriptor.Descriptor(
    name="State",
    full_name="pblczero.State",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="plane",
            full_name="pblczero.State.plane",
            index=0,
            number=1,
            type=6,
            cpp_type=4,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(
                descriptor_pb2.FieldOptions(), _b("\020\001")
            ),
        ),
        _descriptor.FieldDescriptor(
            name="us_ooo",
            full_name="pblczero.State.us_ooo",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="us_oo",
            full_name="pblczero.State.us_oo",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="them_ooo",
            full_name="pblczero.State.them_ooo",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="them_oo",
            full_name="pblczero.State.them_oo",
            index=4,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="side_to_move",
            full_name="pblczero.State.side_to_move",
            index=5,
            number=6,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="rule_50",
            full_name="pblczero.State.rule_50",
            index=6,
            number=7,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=37,
    serialized_end=168,
)


_POLICY = _descriptor.Descriptor(
    name="Policy",
    full_name="pblczero.Policy",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="pblczero.Policy.index",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(
                descriptor_pb2.FieldOptions(), _b("\020\001")
            ),
        ),
        _descriptor.FieldDescriptor(
            name="prior",
            full_name="pblczero.Policy.prior",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(
                descriptor_pb2.FieldOptions(), _b("\020\001")
            ),
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=170,
    serialized_end=216,
)


_GAME = _descriptor.Descriptor(
    name="Game",
    full_name="pblczero.Game",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="state",
            full_name="pblczero.Game.state",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="policy",
            full_name="pblczero.Game.policy",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="pblczero.Game.value",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(
                descriptor_pb2.FieldOptions(), _b("\020\001")
            ),
        ),
        _descriptor.FieldDescriptor(
            name="move",
            full_name="pblczero.Game.move",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=_descriptor._ParseOptions(
                descriptor_pb2.FieldOptions(), _b("\020\001")
            ),
        ),
        _descriptor.FieldDescriptor(
            name="result",
            full_name="pblczero.Game.result",
            index=4,
            number=5,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _GAME_RESULT,
    ],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=219,
    serialized_end=409,
)


_CHUNK = _descriptor.Descriptor(
    name="Chunk",
    full_name="pblczero.Chunk",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="magic",
            full_name="pblczero.Chunk.magic",
            index=0,
            number=1,
            type=7,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="license",
            full_name="pblczero.Chunk.license",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="pblczero.Chunk.version",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="game",
            full_name="pblczero.Chunk.game",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=411,
    serialized_end=522,
)

_GAME.fields_by_name["state"].message_type = _STATE
_GAME.fields_by_name["policy"].message_type = _POLICY
_GAME.fields_by_name["result"].enum_type = _GAME_RESULT
_GAME_RESULT.containing_type = _GAME
_CHUNK.fields_by_name["version"].message_type = net__pb2_ENGINEVERSION
_CHUNK.fields_by_name["game"].message_type = _GAME
DESCRIPTOR.message_types_by_name["State"] = _STATE
DESCRIPTOR.message_types_by_name["Policy"] = _POLICY
DESCRIPTOR.message_types_by_name["Game"] = _GAME
DESCRIPTOR.message_types_by_name["Chunk"] = _CHUNK

State = _reflection.GeneratedProtocolMessageType(
    "State",
    (_message.Message,),
    dict(
        DESCRIPTOR=_STATE,
        __module__="chunk_pb2"
        # @@protoc_insertion_point(class_scope:pblczero.State)
    ),
)
_sym_db.RegisterMessage(State)

Policy = _reflection.GeneratedProtocolMessageType(
    "Policy",
    (_message.Message,),
    dict(
        DESCRIPTOR=_POLICY,
        __module__="chunk_pb2"
        # @@protoc_insertion_point(class_scope:pblczero.Policy)
    ),
)
_sym_db.RegisterMessage(Policy)

Game = _reflection.GeneratedProtocolMessageType(
    "Game",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GAME,
        __module__="chunk_pb2"
        # @@protoc_insertion_point(class_scope:pblczero.Game)
    ),
)
_sym_db.RegisterMessage(Game)

Chunk = _reflection.GeneratedProtocolMessageType(
    "Chunk",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CHUNK,
        __module__="chunk_pb2"
        # @@protoc_insertion_point(class_scope:pblczero.Chunk)
    ),
)
_sym_db.RegisterMessage(Chunk)


_STATE.fields_by_name["plane"].has_options = True
_STATE.fields_by_name["plane"]._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b("\020\001")
)
_POLICY.fields_by_name["index"].has_options = True
_POLICY.fields_by_name["index"]._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b("\020\001")
)
_POLICY.fields_by_name["prior"].has_options = True
_POLICY.fields_by_name["prior"]._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b("\020\001")
)
_GAME.fields_by_name["value"].has_options = True
_GAME.fields_by_name["value"]._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b("\020\001")
)
_GAME.fields_by_name["move"].has_options = True
_GAME.fields_by_name["move"]._options = _descriptor._ParseOptions(
    descriptor_pb2.FieldOptions(), _b("\020\001")
)
# @@protoc_insertion_point(module_scope)
