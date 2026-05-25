---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cultivator|Cultivator]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Cultivator Dedication, Constitution +2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through your disciplined condensations and circulations of qi, you've caught a fleeting glimpse of cultivation's promise, and your health has handsomely profited along the way. You gain the [[Breath Control]], [[Diehard]], and [[Fast Recovery]] feats. You must meet the prerequisites for these feats as normal. For each of these feats you already have, you can instead gain a different feat from the following list: [[Canny Acumen]], [[Fleet]], and [[Toughness]].

**Source:** `= this.source` (`= this.source-type`)
