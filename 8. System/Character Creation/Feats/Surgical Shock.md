---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Attack]]", "[[Investigator]]"]
prerequisites: "forensic medicine methodology"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a few well-placed jabs with your fist or weapon, you render your opponent disoriented or ungainly. Attempt a [[Medicine]] check against the Fortitude DC of a target within your reach. The result of your check determines the severity of the condition you inflict.
- **Critical Success** The target is either [[Clumsy]] 3 or [[Stupefied 3]] until the end of your next turn. The target is then immune to Surgical Shock for 1 hour.
- **Success** As critical success, but the target is either [[Clumsy]] 2 or [[Stupefied 2]].
- **Failure** The target is minorly inconvenienced. You gain a +1 circumstance bonus to the next attack action you attempt against it before the end of your turn.

> [!danger] Effect: Surgical Shock (Failure)
- **Critical Failure** The target is unaffected and you overextend yourself, triggering reactions as if you had used a manipulate action.

**Source:** `= this.source` (`= this.source-type`)
