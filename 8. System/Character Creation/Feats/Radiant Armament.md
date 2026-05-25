---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Champion]]"]
prerequisites: "blessed armament"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your blessed armament radiates power, further enhancing your chosen weapon. When you choose the weapon for your blessed armament during your daily preparations, add the [[Astral]] and [[Brilliant]] property runes to the list of effects you can choose from. If you're holy, also add the [[Holy]] rune, and if you're unholy, also add the [[Unholy]] rune.

In addition, you can change the rune you've selected for the day to a different rune from your list as a 10-minute activity that has the concentrate, divine, and exploration traits. Changing the rune doesn't restore abilities that can be used only a limited number of times, such as Holy Healing for the *holy* rune

> [!danger] Effect: Blessed Armament

**Source:** `= this.source` (`= this.source-type`)
