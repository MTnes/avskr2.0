# Stubs for pathlib (Python 3.5)

from typing import Any, Generator, IO, Optional, Sequence, Tuple, Type, TypeVar, Union
import os

_P = TypeVar('_P', 'PurePath')

class PurePath:
    parts = ...  # type: Tuple[str, ...]
    drive = ...  # type: str
    root = ...  # type: str
    anchor = ...  # type: str
    name = ...  # type: str
    suffix = ...  # type: str
    suffixes = ...  # type: List[str]
    stem = ...  # type: str
    def __new__(cls: Type[_P], *args: Union[str, PurePath]) -> _P: ...
    def __lt__(self, other: PurePath) -> bool: ...
    def __le__(self, other: PurePath) -> bool: ...
    def __gt__(self, other: PurePath) -> bool: ...
    def __ge__(self, other: PurePath) -> bool: ...
    def __truediv__(self: _P, key: Union[str, PurePath]) -> _P: ...
    def __rtruediv__(self: _P, key: Union[str, PurePath]) -> _P: ...
    def __bytes__(self) -> bytes: ...
    def as_posix(self) -> str: ...
    def as_uri(self) -> str: ...
    def is_absolute(self) -> bool: ...
    def is_reserved(self) -> bool: ...
    def match(self, path_pattern: str) -> bool: ...
    def relative_to(self: _P, *other: Union[str, PurePath]) -> _P: ...
    def with_name(self: _P, name: str) -> _P: ...
    def with_suffix(self: _P, suffix: str) -> _P: ...
    def joinpath(self: _P, *other: Union[str, PurePath]) -> _P: ...
    def parents(self: _P) -> Sequence[_P]: ...
    def parent(self: _P) -> _P: ...

class PurePosixPath(PurePath): ...
class PureWindowsPath(PurePath): ...

class Path(PurePath):
    @classmethod
    def cwd(cls: Type[_P]) -> _P: ...
    @classmethod
    def home(cls: Type[_P]) -> _P: ...
    def __new__(cls: Type[_P], *args: Union[str, PurePath], **kwargs: Any) -> _P: ...
    def absolute(self: _P) -> _P: ...
    def stat(self) -> os.stat_result: ...
    def chmod(self, mode: int) -> None: ...
    def exists(self) -> bool: ...
    def expanduser(self: _P) -> _P: ...
    def glob(self, pattern: str) -> Generator[Path, None, None]: ...
    def group(self) -> str: ...
    def is_dir(self) -> bool: ...
    def is_file(self) -> bool: ...
    def is_symlink(self) -> bool: ...
    def is_socket(self) -> bool: ...
    def is_fifo(self) -> bool: ...
    def is_block_device(self) -> bool: ...
    def is_char_device(self) -> bool: ...
    def iterdir(self) -> Generator[Path, None, None]: ...
    def lchmod(self, mode: int) -> None: ...
    def lstat(self) -> os.stat_result: ...
    def mkdir(self, mode: int = ..., parents: bool = ...,
              exist_ok: bool = ...) -> None: ...
    def open(self, mode: str = ..., buffering: int = ...,
             encoding: Optional[str] = ..., errors: Optional[str] = ...,
             newline: Optional[str] = ...) -> IO[Any]: ...
    def owner(self) -> str: ...
    def read_bytes(self) -> bytes: ...
    def read_text(self, encoding: Optional[str] = ...,
                  errors: Optional[str] = ...) -> str: ...
    def rename(self, target: Union[str, PurePath]) -> None: ...
    def replace(self, target: Union[str, PurePath]) -> None: ...
    def resolve(self: _P) -> _P: ...
    def rglob(self, pattern: str) -> Generator[Path, None, None]: ...
    def rmdir(self) -> None: ...
    def samefile(self, other_path: Union[str, bytes, int, Path]) -> bool: ...
    def symlink_to(self, target: Union[str, PurePath],
                   target_is_directory: bool = ...) -> None: ...
    def touch(self, mode: int = ..., exist_ok: bool = ...) -> None: ...
    def unlink(self) -> None: ...
    def write_bytes(self, data: bytes) -> int: ...
    def write_text(self, data: str, encoding: Optional[str] = ...,
                   errors: Optional[str] = ...) -> int: ...


class PosixPath(Path, PurePosixPath): ...
class WindowsPath(Path, PureWindowsPath): ...