---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fire]]", "[[Inventor]]", "[[Modification]]", "[[Unstable]]"]
prerequisites: "armor innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

**Trigger** You would take damage.

Your armor has a retractable spike-covered shell reminiscent of Hwanggot's heavily armored geobukseon, or "turtle ships." The shell unfolds across your body, giving you a +4 circumstance bonus to AC and resistance 2 to bludgeoning, piercing, and slashing damage until the end of your next turn. Spiked chains propelled by small bursts of black powder also erupt from the shell, dealing @Damage[3d4[piercing],2[persistent,fire]|options:area-damage] damage ([[Reflex]] save against your class DC) to all creatures in a @Template[type:emanation|distance:5].

**Source:** `= this.source` (`= this.source-type`)
