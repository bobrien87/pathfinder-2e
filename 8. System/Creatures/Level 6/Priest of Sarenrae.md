---
type: creature
group: ["Holy", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Priest of Sarenrae"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Diplomacy +12, Medicine +14, Religion +14, Society +11, Survival +12"
abilityMods: ["+3", "+3", "+1", "+0", "+4", "+2"]
abilities_top:
  - name: "Healing Hands"
    desc: "When the priest casts [[Heal]], they roll d10s instead of d8s."
  - name: "Steady Spellcasting"
    desc: "If another creature's reaction disrupts the priest's spellcasting action, the priest attempts a DC 15 flat check. If the priest succeeds, their action isn't disrupted."
armorclass:
  - name: AC
    desc: "21; **Fort** +11, **Ref** +13, **Will** +16"
health:
  - name: HP
    desc: "80"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +14 (`pf2:1`) (forceful, magical, sweep), **Damage** 1d6+8 slashing"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+8 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 24, attack +16<br>**3rd** (8 slots) [[Fireball]], [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Heal]], [[Holy Light]], [[Holy Light]]<br>**2nd** (3 slots) [[Resist Energy]], [[Revealing Light]], [[Spiritual Armament]]<br>**1st** (3 slots) [[Breathe Fire]], [[Infuse Vitality]], [[Spirit Link]]<br>**Cantrips** [[Detect Magic]], [[Divine Lance]], [[Light]], [[Read Aura]], [[Vitality Lash]]"
  - name: "Cleric Domain Spells"
    desc: "DC 24, attack +16<br>**1st** [[Dazzling Flash]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Cloistered priests safeguard their temples and communities. They are the stalwart keepers of their god's tenets, devoted to spreading the word. Their guidance or healing services come at the cost of a donation.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Priest of Sarenrae"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
