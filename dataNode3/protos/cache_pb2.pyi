from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataNode(_message.Message):
    __slots__ = ["DN"]
    DN: str
    DN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, DN: _Optional[str] = ...) -> None: ...

class DataNodeSize(_message.Message):
    __slots__ = ["IP", "size"]
    IP: str
    IP_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: str
    def __init__(self, size: _Optional[str] = ..., IP: _Optional[str] = ...) -> None: ...

class ModelInfoWithTime(_message.Message):
    __slots__ = ["name", "segment", "time"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    segment: str
    time: str
    def __init__(self, name: _Optional[str] = ..., segment: _Optional[str] = ..., time: _Optional[str] = ...) -> None: ...

class ObjectWithTime(_message.Message):
    __slots__ = ["name", "object", "segment", "time"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    object: bytes
    segment: str
    time: str
    def __init__(self, name: _Optional[str] = ..., segment: _Optional[str] = ..., time: _Optional[str] = ..., object: _Optional[bytes] = ...) -> None: ...

class boolean(_message.Message):
    __slots__ = ["bool"]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    def __init__(self, bool: bool = ...) -> None: ...

class model(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: bytes
    def __init__(self, object: _Optional[bytes] = ...) -> None: ...

class modelInfo(_message.Message):
    __slots__ = ["name", "segment"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    segment: str
    def __init__(self, name: _Optional[str] = ..., segment: _Optional[str] = ...) -> None: ...

class modelMeta(_message.Message):
    __slots__ = ["name", "segment"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    segment: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[_Iterable[str]] = ..., segment: _Optional[_Iterable[str]] = ...) -> None: ...

class object(_message.Message):
    __slots__ = ["name", "object", "segment"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    object: bytes
    segment: str
    def __init__(self, name: _Optional[str] = ..., segment: _Optional[str] = ..., object: _Optional[bytes] = ...) -> None: ...

class segments(_message.Message):
    __slots__ = ["segment"]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    segment: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, segment: _Optional[_Iterable[str]] = ...) -> None: ...

class serverSpecs(_message.Message):
    __slots__ = ["DN", "storage"]
    DN: str
    DN_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    storage: str
    def __init__(self, DN: _Optional[str] = ..., storage: _Optional[str] = ...) -> None: ...

class text(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class wholeModel(_message.Message):
    __slots__ = ["name", "segment"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    segment: str
    def __init__(self, name: _Optional[str] = ..., segment: _Optional[str] = ...) -> None: ...
