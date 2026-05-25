---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lastwall Sentry|Lastwall Sentry]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "No Stranger to Death"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Though the city of Vigil itself has been destroyed, you will carry on its warrior spirit to the end of your days. The value of your [[Dying]] condition at which you die increases by 1 (normally to dying 5, or dying 6 if you have [[Diehard]]), and the reduction to your maximum dying value from the [[Doomed]] condition is 1 less severe (to a minimum of 0).

**Source:** `= this.source` (`= this.source-type`)
