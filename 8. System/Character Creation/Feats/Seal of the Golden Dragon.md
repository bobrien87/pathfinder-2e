---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Sage|Familiar Sage]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Familiar Sage Dedication, Golden Dragon's Bounty"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would take acid, cold, electricity, poison, fire, or sonic damage.

**Requirements** Your familiar has the resistance ability and is adjacent to you.

Your familiar coils around you, protecting you with its magical resistance. You gain the benefits of your familiar's resistance ability until the start of your next turn. If your familiar has any upgrades to this ability, such as major resistance, you gain them as well. Once per day, if your familiar's resistance is a different damage type, your familiar's resistance ability changes to the appropriate type. If you already have resistance of the same type, choose the higher of the two.

**Source:** `= this.source` (`= this.source-type`)
