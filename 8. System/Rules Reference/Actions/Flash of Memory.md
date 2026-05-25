---
type: action
source-type: "Remaster"
cast: "`pf2:0`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Spend a Mythic Point and attempt an Incarnation Lore check at mythic proficiency to [[Recall Knowledge]] in place of making any other Lore check (other than Incarnation Lore).

**Source:** `= this.source` (`= this.source-type`)
