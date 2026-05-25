---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bounty Hunter|Bounty Hunter]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Bounty Hunter Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're well-versed in weapons that allow you to bring bounties back in one piece, or at least alive. You have familiarity with the [[Bola]], [[Sap]], and [[Whip]]; for the purposes of proficiency, you treat these weapons as simple weapons. You deal an additional 1d4 precision damage with these weapons when using them to make nonlethal Strikes against your prey while they're off-guard to you.

In addition, you take no penalty when making a nonlethal attack with a weapon without the nonlethal trait.

**Source:** `= this.source` (`= this.source-type`)
