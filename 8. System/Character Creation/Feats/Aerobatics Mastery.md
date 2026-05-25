---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "master in Acrobatics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You move with grace in flight and can perform amazing aerial stunts.

You gain a +2 circumstance bonus to Acrobatics checks to [[Maneuver in Flight]] and can combine two maneuvers into a single action, such as reversing direction while making a steep ascent or descent or hovering in gale-force winds. The DC of the Acrobatics check is equal to the DC of the most difficult maneuver + 5.

If you're legendary in Acrobatics, you can combine three such maneuvers into a single action; the DC of the Acrobatics check is equal to the DC of the most difficult maneuver + 10. Regardless of the combination, these maneuvers rarely allow you to move farther than your [[Fly]] Speed.

**Source:** `= this.source` (`= this.source-type`)
