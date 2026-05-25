---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Monk]]", "[[Poison]]"]
prerequisites: "Cobra Stance, expert in unarmed attacks"
frequency: "once per PT1M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Requirements** You are in [[Cobra Stance]].

You slightly dislocate your joints to lash out with devious intent and the power to envenom your foe. Make a cobra fang Strike. Your reach with this Strike is 5 feet greater than normal. If this Strike hits, the persistent poison damage from your venomous trait increases to 1d4 persistent,poison damage per weapon damage die.

**Special** If you have this feat, the circumstance bonus to Fortitude saves and Fortitude DC granted by Cobra Stance increases from +1 to +2.

**Source:** `= this.source` (`= this.source-type`)
