---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wylderheart|Wylderheart]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Wylderheart Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The combination of your passion for both life and the battle against evil makes you graceful and unpredictable. Stride up to your Speed. A creature that attempts a reaction triggered by this movement must first attempt a [[Will]] save against your class DC or spell DC, whichever is higher.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Fascinated]] by you until the end of your next turn.
- **Failure** The creature is fascinated by you until the end of your next turn, but your movements might be too hard to follow; if the reaction requires an attack roll, you gain a +2 circumstance bonus to AC against that attack roll.
- **Critical Failure** The creature is fascinated by you until the end of your next turn, and it loses its reaction.

**Source:** `= this.source` (`= this.source-type`)
