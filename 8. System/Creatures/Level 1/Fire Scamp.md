---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fire Scamp"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+3; [[Darkvision]]"
languages: "Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +7"
abilityMods: ["+0", "+4", "+0", "-2", "+0", "+2"]
abilities_top:
  - name: "Smoke Vision"
    desc: "The fire scamp ignores the [[Concealed]] condition from smoke."
armorclass:
  - name: AC
    desc: "17; **Fort** +3, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "16; fast healing 2 (while touching fire); **Immunities** bleed, paralyzed, poison, sleep, fire; **Weaknesses** cold 3"
abilities_mid:
  - name: "Fast Healing 2 (While Touching Fire)"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse, unarmed), **Damage** 1d4 fire plus 1d6 piercing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 15, attack +7<br>**1st** [[Daze]], [[Ignition]], [[Light]]"
abilities_bot:
  - name: "Flame Breath"
    desc: "`pf2:2` The fire scamp breathes flames in a @Template[cone|distance:15] that deals @Damage[2d4[fire]|options:area-damage] damage to each creature within the area (DC 17 [[Reflex]] save). Creatures that fail the save also take 1d4 persistent,fire damage. <br>  <br> The fire scamp can't use Flame Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Although arguably quite friendly, fire scamps are considered far more dangerous than their kin. They delight in fire and playing pranks on everyone they befriend. Even given time to understand others' dislike of fire, most fire scamps enjoy the feel of flames enough to constantly test their limits.

Compared to the nations of other scamps, the nations on the Plane of Fire are by far the strongest. This backing inspires fire scamps to challenge authority more quickly than the others.

Elemental scamps are bat-like critters marked by elemental powers. Scamps are dispatched from the Elemental Planes by more powerful residents or called to the Universe by neophyte summoners. All scamps have a hint of magical power due to a lingering connection to their home plane, which they largely use to pull simple pranks.

Scamps rapidly form a pecking order of cleverness. Humanoids often confuse scamps when meeting such creatures for the first time. These confused scamps usually resort to an escalating series of pranks and mischief, seeing what they can get away with to establish their place in the hierarchy.

```statblock
creature: "Fire Scamp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
