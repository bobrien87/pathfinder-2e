---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Swashbuckler]]"]
prerequisites: "expert in Athletics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your easily maneuver against your foes. Your [[Disarm]], [[Grapple]], [[Reposition]], [[Shove]], and [[Trip]] actions have a lower multiple attack penalty. Even if your weapon or unarmed attack doesn't have the agile trait, the penalty is –4 if the action is your second attack on your turn, or –8 if it's your third or subsequent attack. If your weapon or unarmed attack is agile and you have panache, the penalty is reduced further, to –3 if it's the second attack on your turn or –6 if it's the third or subsequent.

**Source:** `= this.source` (`= this.source-type`)
