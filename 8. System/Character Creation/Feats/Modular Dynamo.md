---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sterling Dynamo|Sterling Dynamo]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Sterling Dynamo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your dynamo has modular configurations, allowing you to swap between various different possibilities with ease in order to adapt to various situations in combat. Your dynamo attack gains the modular trait, as well as one of the following configurations of your choice: power driver (1d6 bludgeoning damage; shove), percussive striker (1d4 bludgeoning damage; agile, finesse), rotating sickle (1d6 slashing damage; trip), or entangling barbs (1d6 piercing damage; grapple). If you have a manually controlled dynamo, these damage dice increase by 1 size, as usual, and you can also choose the extendable baton (1d4 bludgeoning damage; finesse, reach), which has the damage increase already factored in. When you use an Interact action to switch configurations using the modular trait, you switch between the initial configuration of dynamo you chose with the [[Sterling Dynamo Dedication]] and the new configuration you chose with Modular Dynamo.

**Special** You can select this feat multiple times. Each time, you choose another configuration and add it to the list of options you can choose when you use an Interact action with the modular trait.

**Source:** `= this.source` (`= this.source-type`)
