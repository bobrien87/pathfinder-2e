---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Dwarf]]", "[[Fire]]", "[[Manipulate]]"]
prerequisites: "expert in Crafting"
frequency: "once per PT1M"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Dongun Hold or Alkenstar.

**Frequency** once per minute

You dust explosive black powder on your fist or glove before attacking, which combusts as you hit an opponent. The resulting pops of flame harm both you and your enemy. Until the end of your next turn, your fist loses the nonlethal trait and deals an additional 1 fire damage on a successful Strike. Each time you succeed on a fist Strike, you take 1 fire damage. If your fist would deal more than one weapon damage die, the fire damage dealt on a successful Strike, to both you and your opponent, is equal to the number of weapon damage dice.

**Source:** `= this.source` (`= this.source-type`)
