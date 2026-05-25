---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lion Blade|Lion Blade]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Lion Blade Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned how to move as one with crowds and hide among them, vanishing into a busy street in the flicker of an eye. You move at full Speed in crowds and can use cover from crowds to [[Hide]] and [[Sneak]], gaining a +2 circumstance bonus to your Stealth checks when in a crowd of at least 10 creatures and a +4 circumstance bonus to your Stealth checks when in a crowd of at least 100 creatures.

> [!danger] Effect: Lost in the Crowd

**Source:** `= this.source` (`= this.source-type`)
