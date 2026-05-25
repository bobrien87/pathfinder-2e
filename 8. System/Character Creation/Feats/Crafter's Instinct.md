---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Dwarf]]", "[[Fortune]]"]
prerequisites: "master in Crafting"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Dongun Hold or Alkenstar.

**Frequency** once per day

**Trigger** You misfire with a firearm or you roll a failure on a Strike with a ranged weapon.

You sense a minor flaw in the weapon as you fire it, and quickly adjust your aim on the fly to avoid the flaw. If the triggering Strike was a misfire, you get a normal failure instead. If the triggering Strike was a failure, it becomes a glancing blow that deals minimum damage for the Strike (adding any bonuses as normal but getting a result of 1 for all damage dice that would be rolled on a success). The glancing blow does not apply other effects that would normally happen only on a hit.

**Source:** `= this.source` (`= this.source-type`)
