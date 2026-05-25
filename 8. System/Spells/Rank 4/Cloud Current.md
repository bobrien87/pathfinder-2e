---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "1 minute"
range: "500 feet"
duration: "1 hour"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Air and water vapor combine into a great cloud that funnels a powerful current within it. The eddies make the cloud appear from a distance to be a group of cloud dragons tumbling through the sky. The cloud is up to 30 feet wide, 30 feet tall, and 10 miles long. It runs parallel to the ground, and the nearest end of it must be within range and at least 100 feet above the ground. The current travels in a direction you choose when you Cast the Spell, and the travel Speed of creatures flying through the cloud in that direction is doubled. You can Dismiss the cloud.

**Heightened (6th)** The duration is 8 hours, and the cloud can be up to 50 feet wide and 100 miles long.

**Heightened (8th)** As 6th, and travel speed is quadrupled.

**Source:** `= this.source` (`= this.source-type`)
