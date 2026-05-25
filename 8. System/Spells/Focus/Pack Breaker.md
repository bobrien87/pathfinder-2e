---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Ranger]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You can deceive creatures by changing their perception of their allies' behavior. Each affected creature suspects their allies have changed allegiance, depending on the outcome of their Will save. Regardless of the effects of the saving throw, the creature is then temporarily immune to pack breaker for 1 hour.
- **Critical Success** The creature is unaffected.
- **Success** The creature becomes [[Unfriendly]] to all creatures to which it wasn't already hostile, even those that were previously allies. It treats no one as an ally for 1 minute. Each of its former allies within its reach must attempt a save against pack breaker.
- **Failure** As success, but the creature is also [[Confused]] for 1 round.
- **Critical Failure** As success, but the creature is confused for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
