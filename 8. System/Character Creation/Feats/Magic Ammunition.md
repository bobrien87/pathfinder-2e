---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eldritch Archer|Eldritch Archer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Eldritch Archer Dedication"
frequency: "once per round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You imbue your ammunition with raw and potent magic, transforming it to suit your needs in any situation.

When you select this feat, choose three types of common magical ammunition of 4th level or lower from *GM Core* or this book. Your GM might allow you to choose from other types of magical ammunition of an appropriate level, such as uncommon ammunition, or ammunition from other books. You gain the [[Transform Ammunition]] action.

**Special** You can select this feat multiple times. Each time you do, select three additional types of magical ammunition as described above.

**Source:** `= this.source` (`= this.source-type`)
