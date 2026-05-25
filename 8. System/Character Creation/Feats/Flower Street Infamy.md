---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "11"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "Dandy Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your history of coquetries, flirtations, dalliances, and liaisons is so lengthy that, even in a city as large as Absalom, you're bound to run into your past at inopportune moments. Fortunately, the individual involved might be just as shocked as you are by the unexpected encounter. Choose a target within 30 feet and spin a lascivious tale of how the two of you might have met before. Attempt a [[Deception]] check against the target's Will DC. Regardless of your result, the target is temporarily immune to your Flower Street Infamy for 24 hours.
- **Critical Success** The target is [[Stupefied 3]] for 1 minute.
- **Success** The target is [[Stupefied 2]] for 1 minute.
- **Failure** The target is [[Stupefied 1]] until the start of your next turn.
- **Critical Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
