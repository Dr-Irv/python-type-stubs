from typing import Tuple, Union, Optional, Sequence, overload
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.color import Color
from pygame.rect import Rect

_Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
_ColorValue = Union[Color, Tuple[int, int, int], Sequence[int], int, Tuple[int, int, int, int]]
_RectValue = Union[
    Rect, Union[Tuple[int, int, int, int], Sequence[int]], Union[Tuple[_Coordinate, _Coordinate], Sequence[_Coordinate]],
]

def flip(surface: Surface, xbool: bool, ybool: bool) -> Surface: ...
@overload
def scale(surface: Surface, size: Tuple[int, int], dest_surface: Optional[Surface] = None,) -> Surface: ...
@overload
def scale(surface: Surface, size: Sequence[int], dest_surface: Optional[Surface] = None,) -> Surface: ...
def rotate(surface: Surface, angle: float) -> Surface: ...
def rotozoom(surface: Surface, angle: float, scale: float) -> Surface: ...
def scale2x(surface: Surface, dest_surface: Optional[Surface] = None) -> Surface: ...
@overload
def smoothscale(surface: Surface, size: Tuple[int, int], dest_surface: Optional[Surface] = None,) -> Surface: ...
@overload
def smoothscale(surface: Surface, size: Sequence[int], dest_surface: Optional[Surface] = None,) -> Surface: ...
def get_smoothscale_backend() -> str: ...
def set_smoothscale_backend(value: str) -> None: ...
def chop(surface: Surface, rect: _RectValue) -> Surface: ...
def laplacian(surface: Surface, dest_surface: Surface) -> Surface: ...
@overload
def average_surfaces(
    surfaces: Sequence[Surface],
    dest_surface: Optional[Surface] = None,
    palette_colors: Optional[bool] = True,  # todo: Need to check - it was 1
) -> Surface: ...
@overload
def average_surfaces(
    surfaces: Sequence[Surface], dest_surface: Optional[Surface] = None, palette_colors: Optional[int] = 1,
) -> Surface: ...
def average_color(surface: Surface, rect: Optional[_RectValue]) -> Color: ...
def threshold(
    dest_surface: Surface,
    surf: Surface,
    search_color: _ColorValue,
    threshold: Optional[_ColorValue] = (0, 0, 0, 0),
    set_color: Optional[_ColorValue] = (0, 0, 0, 0),
    set_behavior: Optional[int] = 1,
    search_surf: Optional[Surface] = None,
    inverse_set: Optional[bool] = False,
) -> int: ...
