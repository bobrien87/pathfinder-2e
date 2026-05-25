---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "String Slime"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +11"
abilityMods: ["+4", "-5", "+5", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A string slime can feel nearby motion through vibration and air movement."
  - name: "Weak Acid"
    desc: "A string slime's acid damages only organic material—not metal, stone, or other inorganic substances."
armorclass:
  - name: AC
    desc: "10; **Fort** +12, **Ref** +0, **Will** +5"
health:
  - name: HP
    desc: "90; **Immunities** acid, critical hits, precision, slashing, unconscious, visual, bleed"
abilities_mid:
  - name: "Split"
    desc: "Whenever a string slime would take slashing damage (if it weren't immune) and has at least 10 HP, it splits into two identical slimes with half the original's HP. One string slime is in the same space as the original, and the other appears in an adjacent unoccupied space. If no adjacent space is unoccupied, move smaller creatures and objects out of the way to make a space or the split is canceled at the GM's discretion."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +11 (`pf2:1`) (unarmed), **Damage** 1d8+4 bludgeoning plus 1d6 acid"
spellcasting: []
abilities_bot:
  - name: "Tag Team"
    desc: "`pf2:2` **Requirements** another string slime is within 30 feet <br>  <br> **Effect** The slime arcs protoplasm to the other string slime. Creatures in that line take @Damage[3d6[acid]|options:area-damage] damage with a DC 16 [[Reflex]] save. A creature that fails its save is also knocked [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Found underground or in dungeons, these quivering, slug-like ropes of slime continuously scour their domain for food. In addition to their shape, they are named for their ability to shoot out expanding ribbons of slime that resemble tangled strings.

Slimes, molds, and other oozes can be found in dank dungeons and shadowed forests. While not necessarily evil, some grow to enormous sizes and have insatiable appetites.

```statblock
creature: "String Slime"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
