---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You address an ally or any onlookers to your combat, flaunting to your foes how little attention they require. When you Performance check{Perform}, you can choose single creature within 30 feet and use the following success, critical success, and critical failure effects instead of the normal results; if you do, Perform gains the bravado trait, as well as the auditory and linguistic trait as normal for oration.
- **Critical Success** The target takes a –2 circumstance penalty to attack rolls against creatures other than you until the end of its next turn.
- **Success** The target takes a –1 circumstance penalty to attack rolls against creatures other then you until the end of its next turn.
- **Critical Failure** The target gains a +1 circumstance bonus to attack rolls targeting you until the end of its next turn.

> [!danger] Effect: Enjoy the Show

**Source:** `= this.source` (`= this.source-type`)
