---
type: creature
group: ["Aquatic", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fuath"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Aquatic"
trait_02: "Fey"
trait_03: "Gremlin"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +4, Nature +6, Stealth +7, Thievery +7, Sailing Lore +6"
abilityMods: ["+1", "+4", "+2", "+1", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "18; **Weaknesses** cold iron 2, fire 2"
abilities_mid:
  - name: "Vulnerable to Sunlight"
    desc: "A fuath becomes [[Drained]] 1 (or increases its drained condition by 1) after every consecutive hour they're exposed to sunlight. Being submerged in more than a foot of water prevents the sunlight from harming the fuath."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, finesse), **Damage** 1d6 + 1 slashing"
  - name: "Ranged strike"
    desc: "Dart +9 (`pf2:1`) (agile, range 20 ft.), **Damage** 1d4+1 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +9<br>**1st** [[Create Water]], [[Prestidigitation]], [[Sleep]]"
abilities_bot:
  - name: "Viscous Choke"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The fuath surrounds the head of one air-breathing creature within 30 feet in a magical film of viscous water for 1 minute. The target must succeed at a DC 17 [[Reflex]] save or it begins to choke and must hold its breath to avoid drowning. The film can be temporarily wiped away with a total of 3 Interact actions by the choking creature or creatures adjacent to it, allowing a new Reflex save with a +2 circumstance bonus to end the effect. (These actions don't need to be consecutive or made by the same creature.)"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Despite their small size, fuaths are shipwreckers incarnate. In the dark of night, these gremlins sever ratlines, slash sails, smash sextants, and soil provisions. Once the ship founders, the fuaths return to indulge their craving for land-raised flesh. While fuaths prefer to take their prey asleep, they save a terrible doom for sailors who attack them, surrounding the mariners' faces in magically congealed water to drown them where they stand.

Constantly dripping with water, fuaths have seahorse-like faces, seaweed-green fur over yellow skin, and wicked lobster claws for hands. Lacking the Sakvroth tongue, they have trouble relating to other gremlins aside from hanivers, but they revere sea hags and wicked aquatic fey.

Gremlins arose long ago in the First World, living embodiments of nature's ability to wear away, erode, and decompose. In the Universe, their encounters with mortal civilizations twisted them into creatures devoted to chaos, sabotage, and traps, each variety specializing in a particular brand of mayhem.

```statblock
creature: "Fuath"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
