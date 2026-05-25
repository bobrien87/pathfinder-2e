---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Field Propagandist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You invent a false truth by fast talking, switching arguments, shifting the standard of evidence, and generally confounding others. Choose a creature within 30 feet that you're aware of. Attempt a [[Deception]] check against that target's Will DC. Regardless of your result, the target is temporarily immune to your attempts to Fabricate Truth for 10 minutes.
- **Critical Success** The target becomes [[Stupefied 2]] for 1 round.
- **Success** The target becomes [[Stupefied 1]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
