---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "up to 6 creatures"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The targets experience a day's worth of recovery in an instant. Any detrimental effects that would be gone after 24 hours end, though this doesn't shorten the duration of any active spells affecting the targets. The targets regain Hit Points and recover from conditions as if they had taken 24 hours of rest, but they do not make their daily preparations again or gain any benefits of rest other than healing. The targets are then temporarily immune for 1 day.

**Source:** `= this.source` (`= this.source-type`)
