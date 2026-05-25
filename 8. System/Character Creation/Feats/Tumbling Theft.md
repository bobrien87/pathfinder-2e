---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Acrobatics and Thievery"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You reach for an opponent's item as you move past a foe. If you critically succeed at your check to [[Tumble Through]] an enemy's space, you can attempt to [[Steal]] something from the enemy as a reaction. You gain a +1 circumstance bonus to your Thievery check to Steal as your tumbling make it difficult for your enemy to keep track of your movement. You can Steal any immediately accessible item of light or negligible Bulk on the enemy's person, such as a potion or coin purse hanging from a belt, but not anything inside a container or anything the enemy is holding. The GM has final say on what you can Steal.

**Source:** `= this.source` (`= this.source-type`)
