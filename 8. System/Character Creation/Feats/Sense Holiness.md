---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Champion]]"]
prerequisites: "unholy"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The presence of goodness sickens you with its saccharine self-righteousness. You can sense the presence of creatures with the holy trait within 120 feet. This functions as a vague sense, similar to humans' sense of smell. A holy creature using a disguise or otherwise trying to hide its presence attempts a [[Deception]] check against your Perception DC to hide its sanctification from you. If the creature succeeds at its Deception check, it is then temporarily immune to your Sense Holiness for 1 day.

**Source:** `= this.source` (`= this.source-type`)
