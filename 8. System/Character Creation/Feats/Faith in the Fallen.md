---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Magaambyan Attendant|Magaambyan Attendant]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Magaambyan Attendant Dedication"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're a member of the Vellumis Scholars.

The Gravelands are full of fallen spirits seeking to move on, and you consider it your obligation to assist in that regard. You gain the ability to store spirit wisps in your body, becoming a living *spirit dwelling* (see the Exorcist archetype). Each day during your daily preparations, your *spirit dwelling* attracts a spirit wisp who comes to dwell inside. If your *spirit dwelling* contains no wisps, you can spend 10 minutes in a minor ritual to cast your *spirit dwelling* around an area and attract another wisp. Additionally, you gain a spirit wisp when a haunt or incorporeal undead creature is destroyed within 30 feet of you.

You gain the [[Spirit Sanctification]] action.

Every day before your daily preparations, any spirit wisps remaining within your *spirit dwelling* from the previous day are purified and can continue along the River of Souls.

**Source:** `= this.source` (`= this.source-type`)
