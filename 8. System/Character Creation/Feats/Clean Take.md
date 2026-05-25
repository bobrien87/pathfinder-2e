---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Kitharodian Actor Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You fail, but don't critically fail, a Deception or Performance check to portray a famous figure.

Thanks to many long hours of rehearsals, your acting skill is infinitely adaptable. Even when your impressions don't quite hit the mark, you're able to refine and tweak your performance on the spot. Reroll the triggering check and take the second result.

**Source:** `= this.source` (`= this.source-type`)
