---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Champion]]"]
prerequisites: "Faithful Steed, trained in Survival"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By the grace of your god, your mount can overcome the natural challenges and hazards present in a specific terrain. Choose aquatic, arctic, desert, forest, mountain, plains, sky, swamp, or underground. Your mount must have a swim Speed to select aquatic, and a fly Speed to select sky. Your mount ignores the effects of difficult terrain while in the selected terrain.

If you become an expert in Survival, you can pray during your daily preparations each day to change the type of terrain to which your mount is acclimated.

**Source:** `= this.source` (`= this.source-type`)
