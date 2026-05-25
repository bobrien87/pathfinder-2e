---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Fighter]]", "[[Investigator]]", "[[Ranger]]", "[[Rogue]]"]
prerequisites: "master in Perception"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Fighter, Rogue, Investigator** Your battle instincts make you more aware of [[Concealed]] and [[Invisible]] opponents.

**Ranger** Your heightened senses allow you to instinctively detect unseen opponents.

You don't need to succeed at a flat check to target concealed creatures. You're not [[Off Guard]] to creatures that are [[Hidden]] from you (unless you're off-guard to them for reasons other than the hidden condition), and you need only a successful flat check to target a hidden creature.

While you're adjacent to an [[Undetected]] creature of your level or lower, it is instead only hidden from you.

**Source:** `= this.source` (`= this.source-type`)
