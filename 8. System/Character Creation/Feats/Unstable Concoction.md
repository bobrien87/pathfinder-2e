---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Additive]]", "[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can mix a wondrous yet volatile liquid into an alchemical consumable if it has an initial effect that uses dice. You increase the size of any dice for the item's initial effect by one step. For instance, you could increase damage from a Moderate Alchemist Fire to 2d10 or healing from a Moderate Elixir of Life to 5d8+12. Because this affects only initial dice, it wouldn't increase unarmed attack damage from a bestial mutagen, persistent damage from an acid flask, and the like. When this item is activated, the creature activating it must succeed at a DC 10 flat check or take acid damage equal to the item's level.

**Source:** `= this.source` (`= this.source-type`)
