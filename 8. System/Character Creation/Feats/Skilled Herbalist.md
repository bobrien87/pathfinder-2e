---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Centaur]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've been taught how to craft healing remedies with a variety of herbs and plants. You gain the [[Alchemical Crafting]] feat, except you must select the following items to add to your formula book: [[Antidote (Lesser)]], [[Antiplague (Lesser)]], and [[Elixir of Life (Minor)]], as well as a fourth 1st-level common alchemical formula of your choice. You can use Nature to Craft an alchemical item that has the healing trait, rather than Crafting.

**Source:** `= this.source` (`= this.source-type`)
