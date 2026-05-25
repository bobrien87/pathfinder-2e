---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Striding Fire"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +12"
abilityMods: ["+2", "+5", "+3", "+0", "+4", "+1"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The striding fire ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "24; **Fort** +11, **Ref** +17, **Will** +14"
health:
  - name: HP
    desc: "115; **Immunities** bleed, fire, paralyzed, poison, sleep; **Weaknesses** cold 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, finesse), **Damage** 2d8+5 bludgeoning plus 1d6 fire"
spellcasting: []
abilities_bot:
  - name: "Burning Rush"
    desc: "`pf2:2` The striding fire stretches out its legs to an impossible length, propelling it forward. The striding fire Strides up to double its Speed in a straight line. Its movement during this Stride doesn't trigger reactions. Any creature the striding fire was adjacent to at any point during this Stride must attempt a DC 24 [[Reflex]] save. If it critically fails, it's knocked [[Prone]] by a wave of heated air. The striding fire can't use Burning Rush for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An embodiment of the speed and chaos of a spreading blaze, a striding fire appears as a lithe and long-limbed humanoid composed of shifting-hued flames churning around a skeleton-like framework.

Destructive manifestations of the Plane of Fire, fire elementals sometimes incorporate burning materials into their being or superheated matter, such as molten rock or searing smoke. In combat, they tend to be aggressive and somewhat reckless. Their attacks can sometimes cause major destruction to the surrounding environment, and many fire elementals seem to enjoy seeing their flames spread far and wide.

```statblock
creature: "Striding Fire"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
