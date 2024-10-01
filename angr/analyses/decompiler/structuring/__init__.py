from __future__ import annotations

from .dream import DreamStructurer
from .phoenix import PhoenixStructurer
from .sailr import SAILRStructurer
from .recursive_structurer import RecursiveStructurer


STRUCTURER_CLASSES = {
    SAILRStructurer.NAME: SAILRStructurer,
    PhoenixStructurer.NAME: PhoenixStructurer,
    DreamStructurer.NAME: DreamStructurer,
}

DEFAULT_STRUCTURER = SAILRStructurer


def structurer_class_from_name(name: str) -> type | None:
    return STRUCTURER_CLASSES.get(name.lower(), None)


__all__ = (
    "DreamStructurer",
    "PhoenixStructurer",
    "SAILRStructurer",
    "RecursiveStructurer",
    "STRUCTURER_CLASSES",
    "DEFAULT_STRUCTURER",
    "structurer_class_from_name",
)
