"""All game data migrated from HTML/JS artifacts."""

from .models import (
    ActionCard,
    DynamicCrisis,
    Kingdom,
    KingdomSlot,
    Region,
    RegionCrisis,
    TokenType,
)

# ---------------------------------------------------------------------------
# 24 Action Cards  (from artifacts/print-karten.html)
# ---------------------------------------------------------------------------

ACTION_CARDS: list[ActionCard] = [
    # ⚔️ Militär
    ActionCard(symbol="⚔️", name="Feldzug",     action="Setze alle ⚔️ dieses Stapels ein.",                                              boost="⚔️",    color="#8b2020"),
    ActionCard(symbol="⚔️", name="Belagerung",   action="Setze alle ⚔️🏰 dieses Stapels + 1 🏰 ein.",                                    boost="⚔️ 🏰", color="#8b2020"),
    ActionCard(symbol="⚔️", name="Söldner",      action="Setze alle ⚔️ dieses Stapels + 1 💰 ein. 💰 zählen als ⚔️.",                   boost="⚔️",    color="#8b2020"),
    ActionCard(symbol="⚔️", name="Grenzkampf",   action="Setze alle ⚔️ dieses Stapels + 1 ✝️ ein. Verhindere eine Eskalation.",          boost="⚔️ ✝️", color="#8b2020"),
    # ✝️ Kirche
    ActionCard(symbol="✝️", name="Kreuzzugsbulle", action="Setze alle ✝️ dieses Stapels ein.",                                              boost="✝️",    color="#5a3e8a"),
    ActionCard(symbol="✝️", name="Kirchensegen",   action="Setze alle ✝️👑 dieses Stapels + 1 👑 ein. Ein Mitspieler legt eine Karte neu ab.", boost="✝️ 👑", color="#5a3e8a"),
    ActionCard(symbol="✝️", name="Pilgerweg",      action="Setze alle ✝️🌾 dieses Stapels + 1 🌾 ein.",                                    boost="✝️ 🌾", color="#5a3e8a"),
    ActionCard(symbol="✝️", name="Bischofsrat",    action="Setze alle ✝️ dieses Stapels + 1 ✝️ ein. Schau die oberste Krisenkarte an.",    boost="✝️ 👑", color="#5a3e8a"),
    # 👑 Diplomatie
    ActionCard(symbol="👑", name="Heiratsvertrag",   action="Setze alle 👑 dieses Stapels ein.",                                              boost="👑",    color="#b8860b"),
    ActionCard(symbol="👑", name="Friedensabkommen", action="Setze alle 👑💰 dieses Stapels + 1 💰 ein. Verzögere eine Krise um 1 Runde.",   boost="👑 💰", color="#b8860b"),
    ActionCard(symbol="👑", name="Allianz",          action="Setze alle 👑 dieses Stapels + 1 ✝️ ein. Ein Mitspieler darf eine zweite Karte spielen.", boost="👑", color="#b8860b"),
    ActionCard(symbol="👑", name="Erbfolge",         action="Setze alle 👑🌾 dieses Stapels + 1 👑 ein. Ziehe 1 Karte extra.",               boost="👑 🌾", color="#b8860b"),
    # 💰 Handel
    ActionCard(symbol="💰", name="Tributzahlung",  action="Setze alle 💰 dieses Stapels ein.",                                              boost="💰",    color="#2e6b3e"),
    ActionCard(symbol="💰", name="Handelsroute",   action="Setze alle 💰🌾 dieses Stapels + 1 🌾 ein. Lege eine Karte offen auf anderen Slot.", boost="💰 🌾", color="#2e6b3e"),
    ActionCard(symbol="💰", name="Söldnerwerbung", action="Setze alle 💰 dieses Stapels + 1 ⚔️ ein. 💰 zählen als ⚔️.",                  boost="💰",    color="#2e6b3e"),
    ActionCard(symbol="💰", name="Marktrechte",    action="Setze alle 💰👑 dieses Stapels + 1 👑 ein. Ein Mitspieler darf eine Karte tauschen.", boost="💰 👑", color="#2e6b3e"),
    # 🏰 Burgen
    ActionCard(symbol="🏰", name="Burgbau",       action="Setze alle 🏰 dieses Stapels ein.",                                              boost="🏰",    color="#3a5a8a"),
    ActionCard(symbol="🏰", name="Grenzfestung",  action="Setze alle 🏰⚔️ dieses Stapels + 1 ⚔️ ein. Schütze eine Region vor Eskalation.", boost="🏰 ⚔️", color="#3a5a8a"),
    ActionCard(symbol="🏰", name="Ritterorden",   action="Setze alle 🏰✝️ dieses Stapels + 1 ✝️ ein.",                                   boost="🏰 ✝️", color="#3a5a8a"),
    ActionCard(symbol="🏰", name="Zufluchtsort",  action="Setze alle 🏰🌾 dieses Stapels + 1 🌾 ein. Verhindere Kartenverlust durch Krisen.", boost="🏰 🌾", color="#3a5a8a"),
    # 🌾 Besiedlung
    ActionCard(symbol="🌾", name="Stadtgründung",    action="Setze alle 🌾 dieses Stapels ein.",                                              boost="🌾",    color="#7a6030"),
    ActionCard(symbol="🌾", name="Fuero",             action="Setze alle 🌾👑 dieses Stapels + 1 👑 ein. Stabilisiere eine Region dauerhaft.", boost="🌾 👑", color="#7a6030"),
    ActionCard(symbol="🌾", name="Ernte",             action="Setze alle 🌾💰 dieses Stapels + 1 💰 ein.",                                   boost="🌾 💰", color="#7a6030"),
    ActionCard(symbol="🌾", name="Klostergründung",   action="Setze alle 🌾✝️ dieses Stapels + 1 ✝️ ein. Stabilisiere den ✝️-Slot einer Region.", boost="🌾 ✝️", color="#7a6030"),
]

# ---------------------------------------------------------------------------
# 12 Dynamic Crises  (from artifacts/print-krisen.html)
# ---------------------------------------------------------------------------

DYNAMIC_CRISES: list[DynamicCrisis] = [
    DynamicCrisis(name="Almoravideneinfall",       severity=3, solve="⚔️ + ✝️ + 💰",   immediate="Alle Spieler werfen die oberste Karte eines Slots ab.",                              escalation="Fortschrittsmarker um 1 zurück – eine Region gefährdet."),
    DynamicCrisis(name="Taifa-Verrat",             severity=2, solve="👑 + 💰 + ✝️",    immediate="Kein Spieler darf diese Runde den Kooperationsmoment nutzen.",                       escalation="Ein Spieler verliert eine Karte seiner Wahl."),
    DynamicCrisis(name="Hungersnot",               severity=2, solve="🌾 + 💰 + ⚔️",    immediate="Alle 🌾-Verstärkungen zählen diese Runde nicht.",                                    escalation="Militär-Slot der betroffenen Region wird blockiert."),
    DynamicCrisis(name="Adelsrevolte",             severity=2, solve="👑 + ⚔️ + 💰",    immediate="Kein Spieler darf diese Runde Karten tauschen.",                                     escalation="Ein Spieler legt seinen stärksten Slot für 1 Runde still."),
    DynamicCrisis(name="Kirchenspaltung",          severity=2, solve="✝️ + 👑 + 🌾",    immediate="Alle ✝️-Verstärkungen zählen diese Runde nicht.",                                    escalation="Alle Aktionskarten mit ✝️ können nicht gespielt werden bis gelöst."),
    DynamicCrisis(name="Maurische Gegenoffensive", severity=3, solve="⚔️ + 🏰 + ✝️",   immediate="Sofort eine zweite Krisenkarte aufdecken und würfeln.",                              escalation="Beide betroffenen Regionen eskalieren gleichzeitig."),
    DynamicCrisis(name="Pestwelle",                severity=2, solve="🌾 + ✝️ + 💰",    immediate="Jeder Spieler verliert die unterste Karte eines Slots.",                             escalation="Würfle erneut – Krise breitet sich auf zweite Region aus."),
    DynamicCrisis(name="Erbfolgestreit",           severity=2, solve="👑 + ✝️ + 🌾",    immediate="Zwei Spieler müssen ihre Aktionen dieser Runde tauschen.",                           escalation="Kein Spieler darf von der betroffenen Region Karten nachziehen."),
    DynamicCrisis(name="Dürre",                    severity=1, solve="🌾 + 💰",          immediate="Alle 💰-Aktionen bringen diese Runde die Hälfte.",                                   escalation="💰-Aktionen bleiben halbiert bis gelöst."),
    DynamicCrisis(name="Piratenangriff",           severity=1, solve="⚔️ + 🏰 + 💰",    immediate="Ein zufälliger Spieler muss eine Karte abwerfen.",                                   escalation="Handelsrouten unterbrochen – alle 💰-Aktionen halbiert bis gelöst."),
    DynamicCrisis(name="Ritterorden zerfällt",     severity=2, solve="✝️ + 🏰 + 👑",    immediate="Alle 🏰-Verstärkungen zählen diese Runde nur halb.",                                escalation="Militär-Slot der betroffenen Region dauerhaft geschwächt bis gelöst."),
    DynamicCrisis(name="Inquisition",              severity=3, solve="✝️ + 👑 + 💰",    immediate="Jeder Spieler wirft eine Karte mit ✝️ ab. Hat er keine, verliert er die oberste Karte eines Slots.", escalation="Alle ✝️ zählen nicht als Verstärkung bis gelöst."),
]

# ---------------------------------------------------------------------------
# 6 Fixed Regional Crises  (from artifacts/print-krisen.html)
# ---------------------------------------------------------------------------

REGION_CRISES: list[RegionCrisis] = [
    RegionCrisis(name="Kalifat von Córdoba",     region="Meseta Norte",        solve="⚔️ + ✝️ + 💰",            effect="Blockiert alle Slots in Meseta Norte. Eskaliert nicht."),
    RegionCrisis(name="Taifa-Könige von Toledo", region="Toledo / Tajo",       solve="⚔️ + 👑 + 🌾",            effect="Blockiert alle Slots in Toledo. Eskaliert nicht."),
    RegionCrisis(name="Taifa von Valencia",      region="Valencia / Levante",  solve="⚔️ + 💰 + 🏰",            effect="Blockiert alle Slots in Valencia. Eskaliert nicht."),
    RegionCrisis(name="Almoravidenreich",        region="Extremadura",         solve="⚔️ + 🏰 + ✝️",            effect="Blockiert alle Slots in Extremadura. Eskaliert nicht."),
    RegionCrisis(name="Nasridensultanat",        region="Granada",             solve="⚔️ + ✝️ + 👑 + 🌾",       effect="Blockiert alle Slots in Granada. Liegt über der Belagerung. Eskaliert nicht."),
    RegionCrisis(name="Belagerung von Granada",  region="Granada – Schicht 2", solve="⚔️ + ✝️ + 👑 + 🌾 + 💰", effect="Liegt unter dem Nasridensultanat. Wird erst sichtbar wenn dieses gelöst ist. Eskaliert nicht."),
]

# ---------------------------------------------------------------------------
# 6 Regions  (from artifacts/print-tableaus.html)
# ---------------------------------------------------------------------------

REGIONS: list[Region] = [
    Region(name="Kantabrien / Pyrenäen", sub="Startgebiet – sicher",           color="#4a7c59", w6="–", crisis=False, double=False, start=True),
    Region(name="Meseta Norte",          sub="Fixe Krise: Kalifat von Córdoba", color="#7a9e4e", w6="1", crisis=True,  double=False, start=False),
    Region(name="Toledo / Tajo",         sub="Fixe Krise: Taifa von Toledo",    color="#c8a84b", w6="2", crisis=True,  double=False, start=False),
    Region(name="Valencia / Levante",    sub="Fixe Krise: Taifa von Valencia",  color="#c47a3a", w6="3", crisis=True,  double=False, start=False),
    Region(name="Extremadura",           sub="Fixe Krise: Almoravidenreich",    color="#b05030", w6="4", crisis=True,  double=False, start=False),
    Region(name="Andalusien / Granada",  sub="Nasridensultanat + Belagerung",   color="#a33a2e", w6="5", crisis=True,  double=True,  start=False),
]

# ---------------------------------------------------------------------------
# 4 Kingdoms  (from artifacts/print-tableaus.html)
# ---------------------------------------------------------------------------

KINGDOMS: list[Kingdom] = [
    Kingdom(name="Kastilien", color="#b5451b", desc="Militärische Vormacht der Reconquista", slots=[
        KingdomSlot(label="Slot 1", fixed_symbol="⚔️"),
        KingdomSlot(label="Slot 2", fixed_symbol="⚔️"),
        KingdomSlot(label="Slot 3", fixed_symbol="🌾"),
    ]),
    Kingdom(name="Aragón", color="#d4a017", desc="Meister der Diplomatie und des Handels", slots=[
        KingdomSlot(label="Slot 1", fixed_symbol="👑"),
        KingdomSlot(label="Slot 2", fixed_symbol="💰"),
        KingdomSlot(label="Slot 3", fixed_symbol="👑"),
    ]),
    Kingdom(name="Portugal", color="#2e6b3e", desc="Küstenmacht mit starken Befestigungen", slots=[
        KingdomSlot(label="Slot 1", fixed_symbol="🏰"),
        KingdomSlot(label="Slot 2", fixed_symbol="⚔️"),
        KingdomSlot(label="Slot 3", fixed_symbol="🏰"),
    ]),
    Kingdom(name="Navarra", color="#3a5a8a", desc="Hüter der Kirche und der Pyrenäen", slots=[
        KingdomSlot(label="Slot 1", fixed_symbol="✝️"),
        KingdomSlot(label="Slot 2", fixed_symbol="✝️"),
        KingdomSlot(label="Slot 3", fixed_symbol="👑"),
    ]),
]

# ---------------------------------------------------------------------------
# 7 Token Types  (from artifacts/print-tokens.html)
# ---------------------------------------------------------------------------

TOKEN_TYPES: list[TokenType] = [
    TokenType(emoji="⚔️", name="Militär",     color="#8b2020", light="#fdecea"),
    TokenType(emoji="✝️", name="Kirche",      color="#5a3e8a", light="#f0eafa"),
    TokenType(emoji="👑", name="Diplomatie",  color="#b8860b", light="#fdf8e1"),
    TokenType(emoji="💰", name="Handel",      color="#2e6b3e", light="#e8f5e9"),
    TokenType(emoji="🏰", name="Burgen",      color="#3a5a8a", light="#e8eef8"),
    TokenType(emoji="🌾", name="Besiedlung",  color="#7a6030", light="#fdf5e4"),
    TokenType(emoji="🔺", name="Eskalation",  color="#c0392b", light="#fdecea", count=12),
]
