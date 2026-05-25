---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Jotunborn]]", "[[Manipulate]]", "[[Occult]]"]
frequency: "once per day"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can call upon the ancient powers bestowed on you by the gods to create any tools you might need at a moment's notice. You conjure forth a simple tool, such as a shovel or hammer, into your hands. This tool remains conjured until your next daily preparations so long as it's on your person. If the tool leaves your possession for more than 1 minute, it falls apart into a pile of silk that then dissolves into nothingness.

At 9th level, you can use this ability once per hour instead of once per day. When using it in this way, you can maintain only one tool at a time; any previous tool you conjured dissolves into nothingness.

**Source:** `= this.source` (`= this.source-type`)
