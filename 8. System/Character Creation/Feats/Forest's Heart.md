---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Stance]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your attuned apparition grants Forest Lore or Herbalism Lore as one of its apparition skills.

You adopt a stance that allows your apparitions to channel spiritual energy down through you to inhabit roots, control vines, and command plant-life from the ground you stand on to fight on your behalf. You call forth roots, vines, or other plant growth native to the region and can use them to make unarmed attacks. These deal 4d8 bludgeoning damage, are in the brawling group, and have the finesse, grapple, and reach 30 feet traits. Attacks made with these unarmed attacks don't gain additional damage from striking runes, but can benefit from the item bonus to attack rolls and property runes of [[Handwraps of Mighty Blows]] you wear.

**Source:** `= this.source` (`= this.source-type`)
