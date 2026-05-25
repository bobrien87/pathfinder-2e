---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Poppet]]"]
prerequisites: "tsukumogami poppet heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Not every tool is well cared for, and those that are treated badly might awaken as malevolent spirits. You can temporarily evoke the spirit within a nearby mistreated tool to cast [[Fear]] as a 5th-rank innate arcane spell once per day. When you do so, the terrifying magic of the spell originates from a single unattended object within 30 feet of you instead of from you, and you measure the spell's range from that object. If a target becomes [[Fleeing]] as a result of the spell, they're fleeing from that object instead of from you as their mind fills with the absolute certainty that the object will come to life and attack them with malicious glee.

**Source:** `= this.source` (`= this.source-type`)
