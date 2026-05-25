---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a spike that thrusts up from the earth beneath a target creature, potentially impaling it. The spike is made of cold iron and deals 8d6 piercing damage. The target must attempt a Reflex save.
- **Critical Success** The target dodges the spike and is unaffected.
- **Success** The target is struck by the spike and takes half damage.
- **Failure** The target is impaled through a leg or another nonvital body part. The creature takes full damage and, if it's standing on solid ground, becomes [[Immobilized]]. It can attempt to [[Escape]] (the DC is your spell DC). While it remains impaled, it takes damage from any weakness to cold iron it has at the end of each of its turns.
- **Critical Failure** As failure, but the creature is impaled through a vital organ or its center of mass, taking double damage, and it is [[Off Guard]] as long as it's impaled.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
