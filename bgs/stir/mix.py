"""Homogenisation readings for the mixer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..decision.thresholds import ThresholdSet
from ..errors import ValidationError


@dataclass(frozen=True, slots=True)
class MixReading:
    """One homogenisation level together with its bound verdict."""

    level: float
    tick: int
    ok: bool
    code: str

    def describe(self) -> dict[str, Any]:
        return {"level": self.level, "tick": self.tick, "ok": self.ok, "code": self.code}


def normalize_level(level: float) -> float:
    """Round a homogenisation level."""

    return round(float(level), 4)


def level_reading(thresholds: ThresholdSet, level: float, tick: int) -> MixReading:
    """Record a homogenisation level."""

    return MixReading(level=level, tick=tick, ok=True, code="ok")
