---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Knight Vigilant|Knight Vigilant]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Exploration]]", "[[Skill]]"]
prerequisites: "Knight Vigilant Dedication, legendary in Crafting"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Armor you polish shines with righteous grace. You can take 10 minutes to recite prayers or oaths while polishing a suit of heavy armor that you or a willing creature is wearing. If you do, attempt a DC 35 [[Crafting]] check with the following results. The armor then becomes temporarily immune to this ability until your next daily preparations.
- **Critical Success** Once in the next hour, the creature wearing the polished armor can use a reaction to shine majestically. This reaction is triggered when they would be affected by a spell or ability with the darkness trait. The creature attempts a counteract check against the triggering effect using your Crafting modifier. Additionally, the creature wearing the polished armor gains an additional reaction at the start of each of their turns that can be only used for this reaction.
- **Success** As critical success, but the creature wearing the polished armor doesn't gain an additional reaction at the start of each of their turns.

**Source:** `= this.source` (`= this.source-type`)
