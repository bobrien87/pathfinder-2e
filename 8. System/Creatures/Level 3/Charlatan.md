---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Charlatan"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +8, Deception +11, Diplomacy +9, Occultism +7, Performance +11, Society +7, Stealth +8, Thievery +8, Underworld Lore +9"
abilityMods: ["+0", "+3", "+0", "+2", "+1", "+4"]
abilities_top:
  - name: "Versatile Performance"
    desc: "The charlatan can use their Performance skill to `act make-an-impression skill=performance`, to `act demoralize skill=performance`, and they can use an acting Performance to `act impersonate skill=performance`."
  - name: "Sneak Attack"
    desc: "The charlatan deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +8, **Will** +10"
health:
  - name: HP
    desc: "40"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+2 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+2 bludgeoning"
  - name: "Melee strike"
    desc: "Whip +10 (`pf2:1`) (disarm, finesse, nonlethal, reach, trip), **Damage** 1d4+2 slashing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 20, attack +12<br>**2nd** (2 slots) [[Invisibility]]<br>**1st** (3 slots) [[Charm]], [[Daze]], [[Disguise Magic]], [[Figment]], [[Illusory Disguise]], [[Message]], [[Prestidigitation]], [[Telekinetic Hand]], [[Ventriloquism]]"
  - name: "Bard Composition Spells"
    desc: "DC 19, attack +11<br>**1st** [[Counter Performance]], [[Courageous Anthem]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Charlatans use pretense and misdirection to swindle money and other valuables from the credulous and confused.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Charlatan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
