---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]", "[[Vitality]]", "[[Void]]"]
prerequisites: "trespasser in death's realm"
frequency: "once per PT1H"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Despite the constant cold of death at your back, you keep your gaze forward into the realm of life. You release two @Template[type:cone|distance:15]{15-foot cones}, aimed exactly opposite each other, one ahead of you that deals @Damage[5d10[vitality]|options:area-damage] damage and one behind you that deals @Damage[5d10[void]|options:area-damage] damage, each with a [[Reflex]] save against your class DC. Creatures that critically fail also take 5 persistent damage, of the same damage type dealt (5 persistent,vitality or 5 persistent,void).

**Source:** `= this.source` (`= this.source-type`)
