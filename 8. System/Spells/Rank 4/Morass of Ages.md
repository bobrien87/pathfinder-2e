---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "5-foot emanation"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You surround yourself in temporal eddies that draw out time for those around you, making every step feel like an eternity endured. A creature in the emanation, or that later enters the emanation, must attempt a Fortitude save. The creature attempts this save only once and uses the same effect for the duration of the spell. Each time you Sustain the Spell, you can choose to increase the emanation's radius by 5 feet, to a maximum of 60 feet.
- **Critical Success** The creature is unaffected.
- **Success** Squares in the area are difficult terrain for the creature.
- **Failure** Squares in the area are difficult terrain for the creature, and the creature is [[Slowed]] 1 when it starts its turn in the area.
- **Critical Failure** As failure, plus the creature also becomes [[Restrained]]. The creature can attempt to Escape against your spell DC to remove the restrained condition.

**Source:** `= this.source` (`= this.source-type`)
