---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Sage|Familiar Sage]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Spellshape]]"]
prerequisites: "Familiar Sage Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you weave magic, your familiar traces symbols that throw off fear and doubt. If the next action you use is to Cast a Spell, you or an ally within 30 feet gain a +2 status bonus to saving throws against effects that would cause you to be doomed or frightened for 1 round. At 14th level, you or an ally gain a +3 status bonus to saving throws against these effects instead.

**Source:** `= this.source` (`= this.source-type`)
