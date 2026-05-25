---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Downtime]]", "[[Manipulate]]"]
prerequisites: "trained in Medicine"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

You've studied the routes by which qi flows through the body. The needles stored in your healer's tools can manipulate its flow and improve health when applied to specific meridian points. You spend a day studying an ally to attempt a [[Medicine]] check to improve their qi against a standard DC for your ally's level. The ally is then immune to all uses of Acupuncturist for 1 week.
- **Critical Success** You grant your ally the choice of a +2 circumstance bonus to one downtime activity skill check within the next week, or the ability to roll twice on their next saving throw within the next week against an affliction and take the higher result; this is a fortune effect.
- **Success** You grant your ally a +1 circumstance bonus to one downtime activity skill check within the next week.
- **Critical Failure** Your ally takes a –1 circumstance penalty to all downtime activity skill checks within the next week.

> [!danger] Effect: Acupuncturist

**Source:** `= this.source` (`= this.source-type`)
