---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Commander]]"]
prerequisites: "Officer's Medical Training"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can bandage wounds with the same hand you use to hold your shield. You can use the same hand you are using to wield a shield to [[Treat Wounds]] or use [[Battle Medicine]], and you are considered to have a hand free for other uses of Medicine as long as the only thing you are holding or wielding in that hand is a shield. When you use Battle Medicine on an ally while wielding a shield, they gain a +1 circumstance bonus to AC and Reflex saves that lasts until the start of your next turn or until they are no longer adjacent to you, whichever comes first.

> [!danger] Effect: Shielded Recovery

**Source:** `= this.source` (`= this.source-type`)
