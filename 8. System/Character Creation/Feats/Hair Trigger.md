---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Gunslinger]]"]
prerequisites: "initial deed that allows you to Interact to draw a weapon"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

No one can react faster than you can pull your trigger. When using your initial deed, instead of Interacting to draw a weapon, you can Strike with a firearm or crossbow you're already wielding. If this Strike hits, the target is also [[Off Guard]] until the end of your first turn of the encounter.

**Special** If your initial deed allows you to Interact to draw a weapon more than once, this feat allows you to replace one of these Interact actions and use the other one to draw a weapon. You can't replace both Interact actions with Strikes, but you can draw a loaded firearm or crossbow with one of the actions and immediately shoot it with the other.

**Source:** `= this.source` (`= this.source-type`)
