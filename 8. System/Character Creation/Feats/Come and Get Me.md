---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You open yourself to attacks so you can respond in turn. Until your rage ends, you are [[Off Guard]], and damage rolls against you gain a +2 circumstance bonus. If a creature hits you, that creature is off-guard to you until the end of your next turn. If you hit it before the end of your next turn, you gain temporary Hit Points equal to your Constitution modifier, or double that on a critical hit. These temporary Hit Points last until the end of your rage.

**Source:** `= this.source` (`= this.source-type`)
