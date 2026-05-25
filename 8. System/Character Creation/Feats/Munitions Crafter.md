---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Bullets and bombs can be scarce in some parts, so you've learned to make your own. You become trained in Crafting and gain the advanced alchemy benefits. You can use the advanced alchemy benefits to create a number of daily consumables equal to 4 + half your level (rounded up); these consumables must be bombs or alchemical ammunition.

You gain a formula book that includes the formula for black powder and four 1st-level types of common or uncommon alchemical ammunition or bombs of your choice.

When crafting alchemical ammunition, including black powder in doses or rounds, using advanced alchemy, you create the ammunition in batches of 4 (meaning that if you were 4th level and used all of your advanced alchemy consumables to create alchemical ammunition, you could create a maximum of 24 rounds). You cannot use advanced alchemy to Craft horns or kegs of black powder.

**Source:** `= this.source` (`= this.source-type`)
