---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "1"
traits: ["[[Unholy]]"]
cast: "1 day"
source: "Pathfinder Monster Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call in a favor from one demon of level 2 or lower, two demons of level 0 or lower, or three demons of level –1 or lower.
- **Critical Success** You conjure the demon or demons. They are eager to pursue the task, so they don't ask for a favor.
- **Success** You conjure the demon or demons. They are not eager to pursue the task, so they require a favor in return.
- **Failure** You don't conjure any demons.
- **Critical Failure** The demon or demons are angry that you disturbed them. They appear before you, but they immediately attack you.

**Heightened (+1)** Increase the level of demon you call by 2 for each option.

**Source:** `= this.source` (`= this.source-type`)
