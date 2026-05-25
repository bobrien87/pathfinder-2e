---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Esoterica]]", "[[Thaumaturge]]"]
prerequisites: "Scroll Thaumaturgy"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your esoterica includes scraps of scriptures, magic tomes, druidic markings, and the like, which you can use to create temporary scrolls. Each day during your daily preparations, you can create a single temporary scroll containing a 1st-rank spell of any tradition. The spell must be common, or you must otherwise have access to it. This scroll is an unstable, temporary item and loses its magic the next time you make your daily preparations if you haven't used it by then. It can't be used to Learn the Spell.

At 8th level, add a second temporary scroll containing a 2nd-rank spell.

**Source:** `= this.source` (`= this.source-type`)
