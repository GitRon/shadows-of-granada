"""Data models for Shadows of Granada card game."""

from dataclasses import dataclass, field
from enum import Enum


class Symbol(Enum):
    MILITARY = "⚔️"
    CHURCH = "✝️"
    DIPLOMACY = "👑"
    TRADE = "💰"
    FORTRESS = "🏰"
    SETTLEMENT = "🌾"


class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    @property
    def label(self) -> str:
        return {1: "🟡 Gering", 2: "🟠 Mittel", 3: "🔴 Schwer"}[self.value]


@dataclass(kw_only=True)
class ActionCard:
    symbol: str
    name: str
    action: str
    boost: str
    color: str


@dataclass(kw_only=True)
class DynamicCrisis:
    name: str
    severity: int
    solve: str
    immediate: str
    escalation: str


@dataclass(kw_only=True)
class RegionCrisis:
    name: str
    region: str
    solve: str
    effect: str


@dataclass(kw_only=True)
class Region:
    name: str
    sub: str
    color: str
    w6: str
    crisis: bool
    double: bool
    start: bool


@dataclass(kw_only=True)
class KingdomSlot:
    label: str
    fixed_symbol: str


@dataclass(kw_only=True)
class Kingdom:
    name: str
    color: str
    desc: str
    slots: list[KingdomSlot] = field(default_factory=list)


@dataclass(kw_only=True)
class TokenType:
    emoji: str
    name: str
    color: str
    light: str
    count: int = 12
