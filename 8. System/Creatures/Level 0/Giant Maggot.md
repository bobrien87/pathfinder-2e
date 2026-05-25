---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Maggot"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Tremorsense]] (precise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6"
abilityMods: ["+2", "-1", "+3", "-5", "+1", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "13; **Fort** +9, **Ref** +3, **Will** +3"
health:
  - name: HP
    desc: "15; **Immunities** visual"
abilities_mid:
  - name: "Regurgitation"
    desc: "`pf2:r` **Trigger** The giant maggot takes damage <br>  <br> **Effect** The giant maggot regurgitates its rancid, foul meal. All creatures in a @Template[type:emanation|distance:5] must succeed at a DC 16 [[Fortitude]] save or become [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure). The giant maggot can't use Regurgitation again until it spends at least an hour feeding on a corpse."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +6 (`pf2:1`), **Damage** 1d8+2 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Gnaw Flesh"
    desc: "`pf2:1` **Requirements** The giant maggot has [[Grabbed]] a creature <br>  <br> **Effect** The giant maggot deals @Damage[(1d8+2)[slashing]] damage to the grabbed creature as it chews the creature's flesh (DC 16 [[Reflex]] save)."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Giant flies lay their eggs on the bodies of larger monsters or livestock. When they hatch, these eggs release squirming maggots the size of humans, ravenous young who voraciously consume any flesh in the immediate vicinity—typically starting with the body upon which they were born.

Giant flies are pony-sized insects that have massive compound eyes and bodies bristling with short, stiff hairs. Their lairs are notorious for the rotting meat they stockpile to lay their eggs in. Their maggot dens are also prime breeding grounds for virulent diseases.

```statblock
creature: "Giant Maggot"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
