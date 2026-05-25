---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Monk]]"]
prerequisites: "Crushing Grab, Whirling Throw"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

You have mastered an ultimate grappling technique capable of breaking even the mightiest of foes. You hurl the creature 20 feet into the air, following behind it with a powerful jump, and then make an unarmed Strike. If the Strike is successful, you can repeat this process up to two more times, moving the creature an additional 20 feet directly up into the air with each Strike; the creature keeps the grabbed or restrained condition throughout the sequence. If you miss with any of the Strikes, Godbreaker and the grabbed or restrained condition immediately end and both you and the opponent fall, taking falling damage as normal for the total height of your jump.

If all three Strikes are successful, you immediately grab the creature and bring it crashing to the ground, dealing your unarmed Strike damage plus falling damage to it. You land on your feet adjacent to the creature, you take no damage from the fall, and the creature remains grabbed or restrained by you.

**Source:** `= this.source` (`= this.source-type`)
