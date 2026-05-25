---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "1 day"
source: "Pathfinder Monster Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon an owb to assist you in a goal. Only caligni callers can use this ritual with relative safety. If a different type of caligni attempts this ritual, they use an outcome one degree of success worse than the result of their check. If a non-caligni attempts this ritual, the result is an automatic critical failure.
- **Critical Success** You conjure the owb. It decides your goals closely match its own and doesn't request a favor in return.
- **Success** You conjure the owb. It isn't eager to pursue the task, so it requires a favor in return.
- **Failure** You don't conjure an owb.
- **Critical Failure** You conjure an owb, but it deems you unworthy and siphons away some of your soul energy. All casters become [[Doomed]] 2.

**Source:** `= this.source` (`= this.source-type`)
