---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vehicle Mechanic|Vehicle Mechanic]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Intelligence +2, trained in Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are adept at designing and maintaining mechanical vehicles, and you lavish your attention and ingenuity on one vehicle in particular. You become an expert in Crafting, and you choose one vehicle you own—or your party owns collectively—to be your signature vehicle: the vehicle you spend time customizing to grant it various advantages. You can spend 1 week of downtime with a new vehicle to designate it as your signature vehicle instead. Due to your amazing customizations and adjustments, pilots gain a +1 circumstance bonus to any piloting checks they make to control your signature vehicle. If you are a master in Crafting, this bonus increases to +2.

Vehicle Mechanic

**Source:** `= this.source` (`= this.source-type`)
