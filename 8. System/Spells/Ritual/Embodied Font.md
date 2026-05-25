---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
cast: "1 day"
range: "10 feet"
targets: "the disembodied wildspell associated with the primary caster"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You place the magic items into a neat pile and attempt to draw out their power to form a new body that the target can inhabit.
- **Critical Success** The target materializes within range, with full Hit Points, 1 Mythic Point, and as if having just completed daily preparations.
- **Success** As critical success, but all the target's spells and spell slots are expended.
- **Failure** As success, but the target is [[Clumsy]] 1, [[Drained]] 1, [[Doomed]] 1, and [[Enfeebled]] 1 for 1 week.
- **Critical Failure** The ritual fails and can't be attempted again for that target for 1 week. The magic items are still consumed.

**Source:** `= this.source` (`= this.source-type`)
