---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Dandy Dedication, master in Intimidation"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Your reputation casts a long shadow, allowing you to throw your cultural weight around, especially in larger settlements. With a well-timed tirade or attention-getting shout, you can break a foe's mind and bring them low. Choose a foe within 30 feet, and attempt an [[Intimidation]] check against the target's Will DC. You gain a +1 circumstance bonus to this check if you're in a city or a +2 circumstance bonus to this check if you're in a metropolis. If you're specifically in Absalom, the bonus is instead +3. The target is then temporarily immune to your Do You Know Who I Am? for 24 hours.
- **Critical Success** The target takes 12d6 mental damage and becomes [[Frightened]] 3. It can't reduce its frightened condition below 1 if it ends its turn adjacent to you.
- **Success** The target takes 6d6 mental damage and becomes [[Frightened]] 2.
- **Failure** The target is unaffected.
- **Critical Failure** The target is unaffected, and the embarrassment causes you to take 6d6 mental damage.

**Source:** `= this.source` (`= this.source-type`)
