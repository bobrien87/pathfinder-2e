---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scrounger|Scrounger]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Scrounger Dedication, Magical Crafting"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can [[Craft]] a temporary wondrous item using the magic scrounged from all around. Once per day, you can [[Cobble Together]] a temporary magic item. The temporary item must be common, magical, half your level or lower, and be able to be held, wielded, or worn. Any Craft requirements must be provided as normal.

You can't Cobble Together a consumable, a rune, or an item with runes. If the item must be worn or affixed, removing it once it's affixed or donned destroys it.

**Source:** `= this.source` (`= this.source-type`)
