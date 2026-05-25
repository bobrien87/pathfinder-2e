---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Ranger]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 hunted prey"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your target glows with a magical aura visible only to you and those who follow your lead. Your target is visible to you and others sharing your [[Hunt Prey]] benefits even if it wouldn't normally be due to lighting or the [[Concealed]] or [[Invisible]] conditions, though cover from opaque objects still blocks your sight. You ignore the flat check against the target due to the Concealed condition, and the target isn't automatically [[Hidden]] from you due to darkness or being Invisible.

**Source:** `= this.source` (`= this.source-type`)
