---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "Golden Legionnaire Dedication, expert in Warfare Lore"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You attempt to guide an ally into a more defensive pose against a particular danger. Attempt a Warfare lore check against the hard DC for the level of a creature or hazard you can see. An ally of your choice within 30 feet gains an effect based on the outcome. If you're legendary in Warfare Lore, when you roll a failure or critical failure, you get a success instead.
- **Critical Success** The ally gains a +2 circumstance bonus to AC against the target creature's or hazard's next attack.
- **Success** As critical success, but the bonus is +1.
- **Critical Failure** The ally takes a –1 circumstance penalty to AC against the target creature's or hazard's next attack.

> [!danger] Effect: Commitment to Protection

**Source:** `= this.source` (`= this.source-type`)
