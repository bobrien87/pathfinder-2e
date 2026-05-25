---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scrounger|Scrounger]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Crafting"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While others need specialized tools and a dedicated space, you have found a way to build just about anything, anywhere. You can Craft items even without appropriate tools or a workshop. Additionally, you don't need a physical formula book to remember all of your formulas; you pay the same cost as normal to learn them, but you memorize them all. You gain the [[Cobble Together]] activity.

An item you Cobble Together is a shoddy item, but when creating it you can choose one creature to build it specifically for. That creature doesn't take the normal penalty for using this shoddy item. Your temporary item lasts for 1d4 hours before falling apart into its raw components; the GM rolls the number of hours secretly.

Scrounger

**Source:** `= this.source` (`= this.source-type`)
