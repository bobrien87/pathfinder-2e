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

You make an appeal to a powerful devil, asking them to bind some of their subordinates to your service. If you succeed, the devil sends you their choice of one devil of level 2 or lower, two devils of level 0 or lower, or three devils of level –1 or lower.
- **Critical Success** The devils are sent to you and serve you for 1d4 weeks.
- **Success** The devils are sent to you and serve you for 1d4 days.
- **Failure** Your request is denied.
- **Critical Failure** Not only is your request denied, but the powerful devil sends word of its displeasure to your master.

**Heightened (+1)** Increase the level of devil sent to you by 2 for each option.

**Source:** `= this.source` (`= this.source-type`)
