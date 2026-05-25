---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Jotunborn]]", "[[Manipulate]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have at least one hand free and are adjacent to an ally.

Your giant might allows you to pick up your allies and hurl them across the battlefield. Pick up an adjacent willing ally who is smaller than you and toss them to an unoccupied space you can see within 25 feet; if you have two hands free, you can instead toss them into a space within 30 feet. Your ally's movement doesn't trigger reactions. Your ally ends this movement on their feet and doesn't take damage from the fall. If your ally ends this movement within melee reach of at least one enemy, they can make a melee Strike against an enemy within their reach as a reaction.

**Source:** `= this.source` (`= this.source-type`)
