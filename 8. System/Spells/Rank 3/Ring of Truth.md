---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Detection]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "20-foot burst"
defense: "Will"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You designate an area in which lies are revealed. Creatures in the area also take a –2 status penalty to Deception checks. Each time a creature in the area speaks a true statement, the soft ring of a bell sounds in the area. Creatures are aware of the magic; therefore, they can avoid answering questions to which they would normally respond with a lie, or they can be evasive as long as they remain within the boundaries of the truth. If a creature is in the area when the spell is cast or later enters the area, that creature attempts a Will save. It uses the results of this initial save if it leaves and reenters the area.
- **Critical Success** The target is so convincing that the bell rings even if they lie.
- **Success** If the target lies and succeeds at their Deception check against all targets, the bell still rings.
- **Failure** The bell accurately sees through their deception and will never ring if they lie.

**Source:** `= this.source` (`= this.source-type`)
