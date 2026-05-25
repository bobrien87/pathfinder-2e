---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "10 minutes"
range: "touch"
area: "20-foot burst"
duration: "8 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You ward an area to alert you when creatures enter without your permission. When you cast alarm, select a password. Whenever a Small or larger corporeal creature enters the spell's area without speaking the password, alarm sends your choice of a mental alert (in which case the spell gains the mental trait) or an audible alarm with the sound and volume of a hand bell (in which case the spell gains the auditory trait). Either option automatically awakens you, and the bell allows each creature in the area to attempt a DC 15 [[Perception]] check to wake up. A creature aware of the alarm must succeed at a Stealth check against the spell's DC or trigger the spell when moving into the area.

**Heightened (3rd)** You can specify a trigger for which types of creatures sound the alarm spell.

**Source:** `= this.source` (`= this.source-type`)
