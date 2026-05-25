---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Champion]]"]
prerequisites: "blessed armament"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Add the following property runes to the list you can choose for your blessed armament: [[Animated]], Greater Fearsome, [[Grievous]], [[Keen]], and Greater Vitalizing. If you have the [[Radiant Armament]] feat, add greater Greater Astral and Greater Brilliant to the list as well.

In addition, you can change the rune you've selected for the day to a different rune from your list as a single action that has the concentrate and divine traits. Changing the rune doesn't restore abilities that can be used only a limited number of times.

> [!danger] Effect: Blessed Armament

**Source:** `= this.source` (`= this.source-type`)
