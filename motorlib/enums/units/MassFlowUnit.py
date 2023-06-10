from enum import Enum


# Python 3.11 supports `StrEnum` that would make this a bit more concise to write
# https://docs.python.org/3/library/enum.html#enum.StrEnum
class MassFlowUnit(str, Enum):
    KILOGRAM_PER_SECOND = 'kg/s'
    POUND_PER_SECOND = 'lb/s'
    GRAM_PER_SECOND = 'g/s'
