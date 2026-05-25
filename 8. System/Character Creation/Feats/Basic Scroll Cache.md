---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scroll Trickster|Scroll Trickster]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Scroll Trickster Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a vast and overflowing collection of scroll scraps, riddled with errors and misspellings and leaking energy like a sieve. With enough care, you can coax these scroll scraps into functioning—briefly.

Each day during your daily preparations, you can create a single temporary scroll containing a 1st-rank spell. The spell must be a common spell, a spell to which you have access, or a spell you are able to cast, and you must be trained in the skill corresponding to at least one of the spell's traditions. You can use [[Learn a Spell]] to add spells to those you can use with this feat, even if you aren't a spellcaster. This scroll is an unstable, temporary item and loses its magic the next time you make your daily preparations if you haven't already used it. This temporary scroll can't be used to Learn the Spell.

At 8th level, add a second temporary scroll containing a 2nd-rank spell.

**Source:** `= this.source` (`= this.source-type`)
