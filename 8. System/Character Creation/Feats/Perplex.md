---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Steel Falcon|Steel Falcon]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Steel Falcon Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You weave a confusing web of half-truths, conspiracy theories, and plausible motives to goad an enemy into lashing out wildly. Choose a target within 30 feet that can hear you, and attempt a [[Diplomacy]] check against its Will DC. The creature is then immune to Perplex for 24 hours.
- **Critical Success** The target is [[Stupefied 3]] and [[Confused]] for 1 round.
- **Success** The target is [[Stupefied 1]] for 1 round.
- **Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
