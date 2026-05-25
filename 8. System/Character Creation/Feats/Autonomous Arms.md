---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication, expert proficiency in a spear or polearm"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A portion of the ancient grasping spirit that infuses your being spills over into a spear or polearm you carry. When you perform your daily preparations, choose one spear or polearm you own. This weapon becomes infused with arcane magic and fragments of thought—it doesn't become fully intelligent, but it instinctually recognizes you as its wielder and denies its abilities to any other wielder while you live. If your weapon doesn't possess it already, it gains the effects of the animated property rune. This does not count against the maximum number of property runes your weapon can have at one time. You also gain the [[Call to Hand]] action.

**Source:** `= this.source` (`= this.source-type`)
