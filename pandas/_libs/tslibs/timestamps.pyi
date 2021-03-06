from __future__ import annotations
import sys
from typing import Any, Optional, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

class Timestamp:

    def astimezone(self, *args, **kwargs) -> Timestamp: ...
    def ceil(self, freq: str, ambiguous: Union[bool, str, Literal['raise', 'NaT']] = ...,
                nonexistent: Union[Timedelta, str, Literal['raise', 'shift_forward', 'shift_backward', 'NaT']] = ...) \
            -> Timestamp: ...
    def floor(self, freq: str, ambiguous: Union[bool, str, Literal['raise', 'NaT']] = ...,
                nonexistent: Union[Timedelta, str, Literal['raise', 'shift_forward', 'shift_backward', 'NaT']] = ...) \
            -> Timestamp: ...
    @classmethod
    def combine(cls, date, time) -> Timestamp: ...
    def day_name(self, *args, **kwargs) -> str: ...

    @classmethod
    def fromordinal(cls, ordinal, freq=None, tz=None) -> Timestamp: ...
    @classmethod
    def fromtimestamp(cls, ts: Timestamp) -> Timestamp: ...
    def isoformat(self, *args, **kwargs) -> str: ...
    def month_name(self, locale: str = ...) -> str: ...
    def normalize(self, *args, **kwargs) -> Timestamp: ...
    @classmethod
    def now(cls, tz=None) -> Timestamp: ...
    def replace(self,
                year: Optional[int] = ...,
                month: Optional[int] = ...,
                day: Optional[int] = ...,
                hour: Optional[int] = ...,
                minute: Optional[int] = ...,
                second: Optional[int] = ...,
                microsecond: Optional[int] = ...,
                nanosecond: Optional[int] = ...,
                tzinfo: Optional[Any] = ...,
                fold: int = ...) -> Timestamp: ...
    def round(self, freq: str, ambiguous: Union[bool, str, Literal['raise', 'NaT']] = ...,
                nonexistent: Union[Timedelta, str, Literal['raise', 'shift_forward', 'shift_backward', 'NaT']] = ...) \
            -> Timestamp: ...
    @classmethod
    def today(cls, tz: Optional[Any] = ...) -> Timestamp: ...
    def to_julian_date(self, *args, **kwargs) -> str: ...
    def to_period(self, *args, **kwargs) -> Period: ...
    def tz_convert(self, *args, **kwargs) -> Timestamp: ...
    def tz_localize(self, tz: Any = ...) -> Timestamp: ...
    @classmethod
    def utcfromtimestamp(cls, ts: Timestamp) -> Timestamp: ...
    @classmethod
    def utcnow(cls) -> Timestamp: ...
    def __init__(self, *args, **kwargs): ...
    def __new__(cls, *args, **kwargs) -> Timestamp: ...
    @property
    def dayofweek(self) -> int: ...
    @property
    def dayofyear(self) -> int: ...
    @property
    def daysinmonth(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def freqstr(self) -> str: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def is_month_end(self) -> bool: ...
    @property
    def is_month_start(self) -> bool: ...
    @property
    def is_quarter_end(self) -> bool: ...
    @property
    def is_quarter_start(self) -> bool: ...
    @property
    def is_year_end(self) -> bool: ...
    @property
    def is_year_start(self) -> bool: ...
    @property
    def quarter(self) -> int: ...
    @property
    def week(self) -> int: ...
    @property
    def weekofyear(self) -> int: ...

from .timedeltas import Timedelta
from .period import Period