---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Mythic]]"]
cast: "1 hour"
range: "30 feet"
targets: "all casters involved in ritual"
duration: "24 hours"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The sun rises on a gathering of heroes bonded to a cause. While only one secondary caster can attempt the secondary check, each secondary caster must also spend 1 Mythic Point upon successful completion of the ritual (see below). A secondary caster who chooses not to spend the Mythic Point can't benefit from the ritual's effects.
- **Critical Success** As success, but the first time a caster gains the [[Doomed]], [[Dying]], or [[Wounded]] condition during the ritual's duration, reduce the value of that condition by 1 (minimum 0).
- **Success** Each secondary caster must spend 1 Mythic Point. For the duration of the ritual, when a caster [[Aids]] another caster, they can attempt the associated check at mythic proficiency. On a success, the circumstance bonus the Aiding caster grants is increased to +2, and on a critical success, the circumstance bonus is increased to +5.
- **Failure** The ritual has no effect. The secondary casters don't need to each spend 1 Mythic Point.
- **Critical Failure** The ritual fails, and the casters rupture their own connections to their mythic destinies. None of the casters can gain Mythic Points for 1 week.

**Source:** `= this.source` (`= this.source-type`)
