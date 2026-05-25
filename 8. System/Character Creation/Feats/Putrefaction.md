---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spoil the food and water nearby, even within your foes' bodies. Spend a Mythic Point. Enemies within 60 feet of you must succeed at a [[Fortitude]] save against your class DC or spell DC (whichever is higher) or become [[Sickened]] 1. You also cause edible food to rot and potable water to turn brackish within the area. Choose a number of potions or alchemical elixirs within the area equal to your key attribute modifier and attempt a counteract against each of them using [[Occultism]] check or [[Religion]] check at mythic proficiency. Your counteract rank is half your level. If you succeed, the elixir or potion spoils and becomes a mundane item.

**Source:** `= this.source` (`= this.source-type`)
