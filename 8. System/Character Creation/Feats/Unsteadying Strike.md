---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Commander]]", "[[Flourish]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attack makes your opponent more susceptible to follow-up maneuvers from your allies. Make a melee Strike against an enemy within your reach. If the Strike is successful, the enemy takes a –2 circumstance penalty to their Fortitude DC to resist being Grappled, Repositioned, or Shoved and a –2 circumstance penalty to their Reflex DC to resist being Disarmed. Both penalties last until the start of your next turn.

> [!danger] Effect: Unsteadying Strike

**Source:** `= this.source` (`= this.source-type`)
