---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "0"
traits: ["[[Concentrate]]", "[[Magical]]", "[[Revelation]]"]
prerequisites: "Order of the Scourge"
frequency: "once per day"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

With a moment spent focusing, you can locate the telltale signs of corruption no matter what means it may use to hide from your sight. For 1 minute, you can see through up to 5 feet of stone, wood, or similar barriers as if they didn't exist (though any amount of metal or denser barriers block this effect).

**Source:** `= this.source` (`= this.source-type`)
