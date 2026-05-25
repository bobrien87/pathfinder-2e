---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Bard]]", "[[Cleric]]", "[[Magus]]", "[[Oracle]]", "[[Psychic]]", "[[Sorcerer]]", "[[Witch]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Bard, Oracle, Sorcerer** Study broadens your range of simple spells.

**Cleric** You study a wider range of simple spells.

**Magus, Wizard** Dedicated study allows you to prepare a wider range of simple spells for every situation.

**Psychic** You expand what your mind can accomplish.

**Witch** Your patron recognizes your need for flexibility and versatility, and grants you the power to prepare a wider range of simple spells.

**Prepared** You can prepare two additional cantrips each day.

**Spontaneous** Add two additional cantrips from your spell list to your repertoire.

**Source:** `= this.source` (`= this.source-type`)
