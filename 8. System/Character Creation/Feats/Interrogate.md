---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vindicator|Vindicator]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Vindicator Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You ask questions you know will be answered. Ask a question of a non-allied creature that you can see and have been conversing with. Attempt an Intimidation check against the creature's Will DC; if the creature is a member of the same religion as you, or is an undead or werecreature pretending to be a member of your faith, you get a +2 circumstance bonus on this check. The creature is then temporarily immune for 1 hour.
- **Critical Success** The target must directly answer your question. It doesn't have to answer truthfully, but you gain a +4 circumstance bonus to your Perception DC if the creature attempts to Lie to you.
- **Success** As critical success, but the circumstance bonus is +2.
- **Failure** The target can refuse to answer you and becomes unfriendly if they weren't already unfriendly or hostile.
- **Critical Failure** The target refuses to answer you and becomes hostile if they weren't already. You can't use Interrogate on the target again for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
