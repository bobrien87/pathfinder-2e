---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "1"
cast: "1 day"
source: "Pathfinder Monster Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the powers of Abaddon to grant you the assistance of a div. You call upon a div whose level can be no more than double *div pact*'s spell rank, two divs whose levels are each at least 2 less than double the spell rank, or three divs whose levels are each at least 3 less than double the spell rank.
- **Critical Success** You conjure the div or divs, and they require nothing in return for their service.
- **Success** You conjure the div or divs. They are not eager to pursue the task, so they require a favor in return.
- **Failure** you don't conjure any divs.
- **Critical Failure** You don't conjure any divs, and they send a spiritual backlash that denies your use of any of your innate divine spells for 24 hours. If you are under the effect of any of your innate divine spells, the durations end.

**Source:** `= this.source` (`= this.source-type`)
