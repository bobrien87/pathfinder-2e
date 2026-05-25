---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Designate a single creature that you can see or hear, or whom you've spent a significant amount of time studying and reading about from afar (subject to the GM's approval), and who you know to be an agent of Treerazer. You gain a +2 circumstance bonus to Perception checks to [[Seek]] or [[Sense the Motive]] of this creature. This creature takes a –1 circumstance penalty to saving throws against spells or effects you create; this penalty increases to –2 against effects that have the holy trait.

You can have only one creature designated by Hunt the Razer's Pawn at a time. If you use this ability against a creature when you already have one designated, the prior creature loses the designation and the new creature gains the designation. This lasts until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
