---
type: creature
group: ["Amphibious", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Amoeba Swarm"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Mindless"
trait_03: "Ooze"
trait_04: "Swarm"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Stealth +1"
abilityMods: ["+0", "-2", "+3", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "An amoeba swarm can sense nearby creatures through vibration and air or water movement."
  - name: "Weak Acid"
    desc: "An amoeba's acid damages only organic material-not metal, stone, or other inorganic substances."
armorclass:
  - name: AC
    desc: "9; **Fort** +8, **Ref** +1, **Will** +3"
health:
  - name: HP
    desc: "35; **Immunities** acid, critical hits, precision, unconscious, visual; **Weaknesses** area damage 3, fire 3, splash damage 3; **Resistances** slashing 4, piercing 4"
abilities_mid: []
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Slither"
    desc: "`pf2:1` The amoeba swarm slithers over each creature in its space, dealing @Damage[1d6[acid]|options:area-damage] damage (DC 14 [[Reflex]] save). A creature that critically fails is [[Sickened]] 1."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

An amoeba swarm consists of thousands of individual single-celled organisms held together by acrid-smelling slime. As ravenous as they are mindless, amoeba swarms use no tactics.

```statblock
creature: "Amoeba Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
