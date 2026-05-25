---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Additive]]", "[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can add the full ingredients of a second elixir to an elixir you make to create a hybrid concoction. You must expend an additional versatile vial to make this combined elixir, and the ingredients must be for an elixir of the same level or lower that you could create with [[Quick Alchemy]]. When this combination elixir is consumed, both the constituent elixirs take effect. For example, you can combine two Lesser Elixirs of Life to create a combined elixir that heals twice the normal amount, or you can combine a Lesser Darkvision Elixir with a Lesser Eagle-Eye Elixir to both gain darkvision and find secret doors.

**Source:** `= this.source` (`= this.source-type`)
