---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "1 minute"
area: "60-foot emanation"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This spell compels local spirits to reenact a violent event of the recent past that you're aware of and name as you Cast the Spell. You take the role of the primary victim. The reenactment plays out the final 9 minutes leading up to the death or injury of the victim and the minute after. The spirits don't change form, so this doesn't help determine perpetrators by their looks. Spiritual forms of missing creatures necessary for the event manifest as needed, and missing items appear as shadowy outlines.

Once the scene ends, you take 2d6 void damage for each ghostly apparition that participated in the scene (typically equal to the number of creatures involved other than the victim). Any creature that observed the ghostly recreation, including you, can attempt checks to investigate the event to discover new clues and information.

**Source:** `= this.source` (`= this.source-type`)
