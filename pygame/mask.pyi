from typing import Optional, Union, Text, Tuple, TypeVar, Sequence, overload

from pygame.math import Vector2
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.color import Color

_Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
_ColorValue = Union[Color, Tuple[int, int, int], Sequence[int], int, Tuple[int, int, int, int]]
_ToSurfaceColorValue = Union[Color, Tuple[int, int, int], Sequence[int], int, Text, Tuple[int, int, int, int]]
_RectValue = Union[
    Rect, Union[Tuple[int, int, int, int], Sequence[int]], Union[Tuple[_Coordinate, _Coordinate], Sequence[_Coordinate]],
]
_Offset = TypeVar("_Offset", Tuple[int, int], Sequence[int])

def from_surface(surface: Surface, threshold: Optional[int] = 127) -> Mask: ...
def from_threshold(
    surface: Surface,
    color: _ColorValue,
    threshold: Optional[_ColorValue] = (0, 0, 0, 255),
    other_surface: Optional[Surface] = None,
    palette_colors: Optional[int] = 1,
) -> Mask: ...

class Mask:
    @overload
    def __init__(self, size: Sequence[int], fill: Optional[bool] = False) -> None: ...
    @overload
    def __init__(self, size: Tuple[int, int], fill: Optional[bool] = False) -> None: ...
    def copy(self) -> Mask: ...
    def get_size(self) -> Tuple[int, int]: ...
    def get_rect(self, **kwargs) -> Rect: ...  # Dict type needs to be completed
    @overload
    def get_at(self, pos: Sequence[int]) -> int: ...
    @overload
    def get_at(self, pos: Tuple[int, int]) -> int: ...
    @overload
    def set_at(self, pos: Sequence[int], value: Optional[int] = 1) -> None: ...
    @overload
    def set_at(self, pos: Tuple[int, int], value: Optional[int] = 1) -> None: ...
    def overlap(self, othermask: Mask, offset: _Offset) -> Union[Tuple[int, int], None]: ...
    def overlap_area(self, othermask: Mask, offset: _Offset) -> int: ...
    def overlap_mask(self, othermask: Mask, offset: _Offset) -> Mask: ...
    def fill(self) -> None: ...
    def clear(self) -> None: ...
    def invert(self) -> None: ...
    @overload
    def scale(self, size: Sequence[int]) -> Mask: ...
    @overload
    def scale(self, size: Tuple[int, int]) -> Mask: ...
    def draw(self, othermask: Mask, offset: _Offset) -> None: ...
    def erase(self, othermask: Mask, offset: _Offset) -> None: ...
    def count(self) -> int: ...
    def centroid(self) -> Tuple[int, int]: ...
    def angle(self) -> float: ...
    def outline(self, every: Optional[int] = 1) -> Sequence[Tuple[int, int]]: ...
    def convolve(self, othermask: Mask, outputmask: Optional[Mask] = None, offset: Optional[_Offset] = (0, 0),) -> Mask: ...
    @overload
    def connected_component(self, pos: Sequence[int] = [-1, -1]) -> Mask: ...
    @overload
    def connected_component(self, pos: Tuple[int, int] = (-1, -1)) -> Mask: ...
    def connected_components(self, min: Optional[int] = 0) -> Sequence[Mask]: ...
    def get_bounding_rects(self) -> Rect: ...
    @overload
    def to_surface(
        self,
        surface: Optional[Surface] = None,
        setsurface: Optional[Surface] = None,
        unsetsurface: Optional[Surface] = None,
        setcolor: Optional[_ToSurfaceColorValue] = (255, 255, 255, 255),
        unsetcolor: Optional[_ToSurfaceColorValue] = (0, 0, 0, 255),
        dest: Optional[_RectValue] = (0, 0),
    ) -> Surface: ...
    @overload
    def to_surface(
        self,
        surface: Optional[Surface] = None,
        setsurface: Optional[Surface] = None,
        unsetsurface: Optional[Surface] = None,
        setcolor: Optional[_ToSurfaceColorValue] = (255, 255, 255, 255),
        unsetcolor: Optional[_ToSurfaceColorValue] = (0, 0, 0, 255),
        dest: Optional[_Coordinate] = (0, 0),
    ) -> Surface: ...
