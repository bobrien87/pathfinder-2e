---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Divine]]", "[[Dwarf]]"]
prerequisites: "worshipper of Torag or Angradd"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Dongun Hold or Alkenstar.

**Frequency** once per day

**Trigger** You attempt a ranged Strike.

You intone a prayer to the dwarven deities Torag or Angradd, willing a higher power to guide your aim in the heat of battle. On your next Strike with a ranged weapon before the end of your turn, you gain a +2 circumstance bonus to your attack roll and ignore your target's [[Concealed]] condition, as well as your target's lesser, standard, and greater cover.

**Source:** `= this.source` (`= this.source-type`)
