---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Linguist|Linguist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Linguist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Even if you don't speak a creature's language, you can rely on inflection, root words, and body language to infer rudimentary meaning.

If you interact with a creature for at least 10 minutes and that creature can speak a language, the GM rolls a secret Society check with a DC appropriate for the language's rarity.

On a success, you understand the gist of the meaning and can communicate basic concepts back to the creature; on a failure, you are mistaken or communicate incorrect concepts.

If you're legendary in Society, you can communicate instantly without needing to attempt a Society check; even if you didn't know the medium of communication the creature uses (speech, sign language, and so on), you intuit this information as soon as they try to communicate.

**Source:** `= this.source` (`= this.source-type`)
