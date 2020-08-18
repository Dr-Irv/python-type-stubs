from typing import (
    Any, Mapping, Sequence,
    Union,
    Tuple,
    Optional,
    Callable,
    SupportsFloat,
    Iterator,
    overload,
)

from pygame.rect import Rect
from pygame.surface import Surface

_RectStyle = Union[
    Tuple[float, float, float, float], Tuple[Tuple[float, float], Tuple[float, float]], Sequence[float], Rect,
]

# Some functions violate Liskov substitution principle so mypy will throw errors for this file, but this are the
# best type hints I could do

class Sprite:
    image: Optional[Surface] = None
    rect: Optional[Rect] = None
    def __init__(self, *groups: AbstractGroup) -> None: ...
    def update(self, *args, **kwargs) -> None: ...
    def add(self, *groups: AbstractGroup) -> None: ...
    def remove(self, *groups: AbstractGroup) -> None: ...
    def kill(self) -> None: ...
    def alive(self) -> bool: ...
    def groups(self) -> Sequence[AbstractGroup]: ...

class DirtySprite(Sprite):
    dirty: int
    blendmode: int
    source_rect: Rect
    visible: int
    _layer: int
    def _set_visible(self, value: int) -> None: ...
    def _get_visible(self) -> int: ...

class AbstractGroup:
    spritedict = Mapping[Sprite, int]
    lostsprites = Sequence[int]  # I think
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Sprite]: ...
    def copy(self) -> AbstractGroup: ...
    def sprites(self) -> Sequence[Sprite]: ...
    def add(self, *sprites: Sprite) -> None: ...
    def remove(self, *sprites: Sprite) -> None: ...
    def has(self, *sprites: Sprite) -> bool: ...
    def update(self, *args, **kwargs) -> None: ...
    def draw(self, surface: Surface) -> None: ...
    def clear(self, surface_dest: Surface, background: Surface) -> None: ...
    def empty(self) -> None: ...

class Group(AbstractGroup):
    def __init__(self, *sprites: Sprite) -> None: ,,,
    def copy(self) -> Group: ...

class RenderPlain(Group):
    def copy(self) -> RenderPlain: ...

class RenderClear(Group):
    def copy(self) -> RenderClear: ...

class RenderUpdates(Group):
    def copy(self) -> RenderUpdates: ...
    def draw(self, surface: Surface) -> Sequence[Rect]: ...

class OrderedUpdates(RenderUpdates):
    def copy(self) -> OrderedUpdates: ...

class LayeredUpdates(AbstractGroup):
    def __init__(self, *sprites: Sprite, **kwargs: Mapping[str, Any]) -> None: ...
    def copy(self) -> LayeredUpdates: ...
    def add(self, *sprites: Sprite, **kwargs: Mapping[str, Any]) -> None: ...
    def draw(self, surface: Surface) -> Sequence[Rect]: ...
    @overload
    def get_sprites_at(self, pos: Tuple[int, int]) -> Sequence[Sprite]: ...
    @overload
    def get_sprites_at(self, pos: Sequence[int]) -> Sequence[Sprite]: ...
    def get_sprite(self, idx: int) -> Sprite: ...
    def remove_sprites_of_layer(self, layer_nr: int) -> Sequence[Sprite]: ...
    def layers(self) -> Sequence[int]: ...
    def change_layer(self, sprite: Sprite, new_layer: int) -> None: ...
    def get_layer_of_sprite(self, sprite: Sprite) -> int: ...
    def get_top_layer(self) -> int: ...
    def get_bottom_layer(self) -> int: ...
    def move_to_front(self, sprite: Sprite) -> None: ...
    def move_to_back(self, sprite: Sprite) -> None: ...
    def get_top_sprite(self) -> Sprite: ...
    def get_sprites_from_layer(self, layer: int) -> Sequence[Sprite]: ...
    def switch_layer(self, layer1_nr: Any, layer2_nr: Any) -> None: ... # not clear of layer*_nr is a number or a sprite

class LayeredDirty(LayeredUpdates):
    def __init__(self, *sprites: DirtySprite, **kwargs: Mapping[str, Any]) -> None: ...
    def copy(self) -> LayeredDirty: ...
    def draw(self, surface: Surface, bgd: Optional[Surface] = None) -> Sequence[Rect]: ...
    def clear(self, surface: Surface, bgd: Surface) -> None: ...
    def repaint_rect(self, screen_rect: _RectStyle) -> None: ...
    def set_clip(self, screen_rect: Optional[_RectStyle] = None) -> None: ...
    def get_clip(self) -> Rect: ...
    def set_timing_treshold(self, time_ms: SupportsFloat) -> None: ...  # This actually accept any value

class GroupSingle(AbstractGroup):
    sprite: Sprite
    def __init__(self, sprite: Optional[Sprite]) -> None: ...
    def copy(self) -> GroupSingle: ...

def spritecollide(
    sprite: Sprite, group: AbstractGroup, dokill: bool, collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> Sequence[Sprite]: ...
def collide_rect(left: Sprite, right: Sprite) -> bool: ...

class collide_rect_ratio:
    ratio: float
    def __init__(self, ratio: float) -> None: ...
    def __call__(self, left: Sprite, right: Sprite) -> bool: ...

def collide_circle(left: Sprite, right: Sprite) -> bool: ...

class collide_circle_ratio:
    ratio: float
    def __init__(self, ratio: float) -> None: ...
    def __call__(self, left: Sprite, right: Sprite) -> bool: ...

def collide_mask(sprite1: Sprite, sprite2: Sprite) -> Tuple[int, int]: ...
def groupcollide(
    group1: AbstractGroup,
    group2: AbstractGroup,
    dokill: bool,
    dokill2: bool,
    collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> Mapping[Sprite, Sprite]: ...
def spritecollideany(
    sprite: Sprite, group: AbstractGroup, collided: Optional[Callable[[Sprite, Sprite], bool]] = None,
) -> Sprite: ...

