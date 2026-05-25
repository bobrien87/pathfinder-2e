---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Shared Archetype Feats|Shared Archetype Feats]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Acrobat, Celebrity, Dandy, or Gladiator Dedication"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your training has focused you for the opera, and it certainly shows. You become master in Performance, and at 15th level your skill in Performance increases to Legendary. You also become expert in Theater Lore or become master in Theater Lore if you were already expert. When you're on a stage, in an arena, or otherwise at the focus of a crowd there to see you perform, your eagerness to begin grants a +3 circumstance bonus to initiative rolls if you roll Acrobatics, Intimidation, or Performance for initiative.

**Source:** `= this.source` (`= this.source-type`)
