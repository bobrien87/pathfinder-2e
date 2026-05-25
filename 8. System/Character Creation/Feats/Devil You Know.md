---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Hellbreaker Dedication, expert in Devil Lore or Hellknight Lore"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your knowledge of your enemies gives you an advantage against them, granting you a swift reaction to their devilry. If you know you're fighting against any devils or Hellknights at the beginning of an encounter, you can roll the respective Lore skill for your initiative roll.

In addition, whenever you successfully Recall Knowledge about a creature using Devil Lore or Hellknight Lore, you gain a +1 circumstance bonus to your next skill check against that creature before the end of your next turn. If you're a master in Devil Lore or Hellknight Lore, the bonus increases to +2.

> [!danger] Effect: Devil You Know

**Source:** `= this.source` (`= this.source-type`)
