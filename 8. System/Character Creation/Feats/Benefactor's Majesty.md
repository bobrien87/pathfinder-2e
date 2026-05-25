---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Healing]]", "[[Kobold]]", "[[Visual]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You tap into the grandeur of your warren's benefactor. You gain temporary Hit Points equal to your level, which last for 1 minute. In addition, you can immediately attempt a flat check to remove each type of persistent damage you have. Finally, until the start of your next turn, any creature targeting you with a harmful attack, spell, or ability much first succeed at a DC 11 flat check or the action is disrupted as the creature avoids setting eyes upon your majesty.

**Source:** `= this.source` (`= this.source-type`)
