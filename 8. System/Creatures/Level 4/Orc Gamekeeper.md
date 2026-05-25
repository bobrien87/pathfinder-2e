---
type: creature
group: ["Humanoid", "Orc"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orc Gamekeeper"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Athletics +13, Diplomacy +9, Nature +13, Stealth +12, Survival +11"
abilityMods: ["+3", "+4", "+0", "+0", "+3", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "65"
abilities_mid:
  - name: "Insistent Command"
    desc: "When the gamekeeper rolls a success to `act command-an-animal`, they get a critical success instead; if they roll a critical failure, they get a failure instead."
  - name: "Play Chicken"
    desc: "`pf2:r` **Trigger** An adjacent enemy misses the gamekeeper with melee attack <br>  <br> **Effect** The gamekeeper attempts to capture the flailing assailant. They attempt an Athletics check to `act grapple` the attacker."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bola +14 (`pf2:1`) (nonlethal, ranged trip, thrown 20), **Damage** 1d6+9 bludgeoning"
  - name: "Melee strike"
    desc: "Whip +14 (`pf2:1`) (disarm, finesse, nonlethal, reach, trip), **Damage** 1d4+9 slashing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Animal Tandem"
    desc: "`pf2:2` The orc gamekeeper makes a Strike against a creature adjacent to one of the gamekeeper's animal allies. If it hits, the animal ally deals one die of damage to the target, using the highest damage die among its unarmed attacks."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Gamekeepers live on the outskirts of the hold, usually remaining solitary and tending to animals they've captured. Every part of a trapped animal can be useful for making supplies or trading.

Orcs have a strict moral code encompassing valor and accomplishment, and they cast out those unwilling to follow it. For the last few generations, orcs have been trying to erase the narratives around their culture as being solely focused on war and violence. They invite other races and adventuring parties inside their holds so they may experience the truth of who the orcs are.

```statblock
creature: "Orc Gamekeeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
