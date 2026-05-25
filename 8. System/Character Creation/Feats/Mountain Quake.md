---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Monk]]"]
prerequisites: "Mountain Stronghold"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Mountain Stance]]

You stomp, shaking the earth beneath you. Creatures on the ground within a @Template[emanation|distance:20] take damage equal to your Strength modifier (minimum 0), with a [[Fortitude]] save against your class DC. On a failure, they also fall [[Prone]]. After you use this action, you can't use it again for 1d4 rounds.

**Special** If you have this feat, the Dexterity modifier cap to your AC while using Mountain Stance increases from +1 to +2.

**Source:** `= this.source` (`= this.source-type`)
