---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eldritch Archer|Eldritch Archer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Eldritch Archer Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have learned to mimic the power that lies between magic and material. You enchant a piece of ammunition on your person with the magical essence of a precious material, allowing you to leverage certain creatures' weaknesses.

Choose cold iron or silver; if you shoot the arrow or bolt before the end of your turn, it counts as that material. At 14th level, add adamantine to the list of materials you can choose from.

**Source:** `= this.source` (`= this.source-type`)
