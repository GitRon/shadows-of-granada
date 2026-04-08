# Shadows of Granada

**Reconquista** – a cooperative card game for 2-4 players set during the Spanish Reconquista.

## Overview

Players control one of four Iberian kingdoms (Kastilien, Aragon, Portugal, Navarra) working together to reclaim the peninsula region by region, from Kantabrien in the north to Granada in the south. Dynamic crises threaten progress each round while fixed regional crises must be overcome to conquer new territory.

## Components

| Component | Count | Description |
|---|---|---|
| Action cards | 24 | 4 per symbol, shared deck |
| Dynamic crises | 12 | Random events each round |
| Regional crises | 6 | Fixed on Muslim-held regions |
| Kingdom tableaus | 4 | 3 card slots each with printed starting reinforcement |
| Symbol tokens | 72 | 12 per symbol type |
| Escalation markers | 12 | Track unresolved crises |
| Shared tableau | 1 | 6 regions north to south |

## Symbols

| Symbol | Name | Domain |
|---|---|---|
| ⚔️ | Militar | Battles, sieges, defense |
| ✝️ | Kirche | Legitimacy, morale, papal support |
| 👑 | Diplomatie | Alliances, marriage politics |
| 💰 | Handel | Finance, tributes, mercenaries |
| 🏰 | Burgen | Border security, fortification |
| 🌾 | Besiedlung | Population, agriculture, stability |

## Project structure

```
shadows-of-granada/
├── artifacts/              # Original HTML prototypes (reference)
├── shadows_of_granada/
│   ├── __init__.py
│   ├── models.py           # Dataclass definitions
│   ├── data.py             # All game data
│   ├── render.py           # Jinja2 → HTML renderer
│   └── templates/          # Jinja2 templates
│       ├── karten.html.j2
│       ├── krisen.html.j2
│       ├── tableaus.html.j2
│       ├── tokens.html.j2
│       └── regelwerk.html.j2
├── output/                 # Generated HTML (gitignored)
├── pyproject.toml
└── README.md
```

## Usage

```bash
pip install -e .
render-cards          # writes HTML files to output/
```

Or run directly:

```bash
python -m shadows_of_granada.render
```
