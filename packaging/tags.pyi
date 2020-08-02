from ._typing import TYPE_CHECKING as TYPE_CHECKING, cast as cast
from typing import Any, Dict, FrozenSet, IO, Iterable, Iterator, Optional, Sequence, Tuple

PythonVersion = Sequence[int]
MacVersion = Tuple[int, int]
GlibcVersion = Tuple[int, int]
logger: Any
INTERPRETER_SHORT_NAMES: Dict[str, str]

class Tag:
    def __init__(self, interpreter: str, abi: str, platform: str) -> None: ...
    @property
    def interpreter(self) -> str: ...
    @property
    def abi(self) -> str: ...
    @property
    def platform(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

def parse_tag(tag: str) -> FrozenSet[Tag]: ...
def cpython_tags(python_version: Optional[PythonVersion]=..., abis: Optional[Iterable[str]]=..., platforms: Optional[Iterable[str]]=..., **kwargs: bool) -> Iterator[Tag]: ...
def generic_tags(interpreter: Optional[str]=..., abis: Optional[Iterable[str]]=..., platforms: Optional[Iterable[str]]=..., **kwargs: bool) -> Iterator[Tag]: ...
def compatible_tags(python_version: Optional[PythonVersion]=..., interpreter: Optional[str]=..., platforms: Optional[Iterable[str]]=...) -> Iterator[Tag]: ...
def mac_platforms(version: Optional[MacVersion]=..., arch: Optional[str]=...) -> Iterator[str]: ...

class _ELFFileHeader:
    class _InvalidELFFileHeader(ValueError): ...
    ELF_MAGIC_NUMBER: int = ...
    ELFCLASS32: int = ...
    ELFCLASS64: int = ...
    ELFDATA2LSB: int = ...
    ELFDATA2MSB: int = ...
    EM_386: int = ...
    EM_S390: int = ...
    EM_ARM: int = ...
    EM_X86_64: int = ...
    EF_ARM_ABIMASK: int = ...
    EF_ARM_ABI_VER5: int = ...
    EF_ARM_ABI_FLOAT_HARD: int = ...
    e_ident_magic: Any = ...
    e_ident_class: Any = ...
    e_ident_data: Any = ...
    e_ident_version: Any = ...
    e_ident_osabi: Any = ...
    e_ident_abiversion: Any = ...
    e_ident_pad: Any = ...
    e_type: Any = ...
    e_machine: Any = ...
    e_version: Any = ...
    e_entry: Any = ...
    e_phoff: Any = ...
    e_shoff: Any = ...
    e_flags: Any = ...
    e_ehsize: Any = ...
    e_phentsize: Any = ...
    e_phnum: Any = ...
    e_shentsize: Any = ...
    e_shnum: Any = ...
    e_shstrndx: Any = ...
    def __init__(self, file: IO[bytes]): ...

def interpreter_name() -> str: ...
def interpreter_version(**kwargs: bool) -> str: ...
def sys_tags(**kwargs: bool) -> Iterator[Tag]: ...