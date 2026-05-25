---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Linguist|Linguist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Linguistic]]"]
prerequisites: "Linguist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Another creature within 60 feet uses a linguistic effect in a language you understand.

You bridge a language gap, repeating the message in a different language that you know. Choose a language you understand to repeat the message in. The linguistic effect counts as both languages, rather than only the language the triggering creature is using, potentially allowing it to affect a wider range of creatures. As normal, you can translate normal speech without Spot Translate and without using a reaction, but this reaction allows you to apply the benefits of translation to spells and actions such as command or [[Demoralize]].

**Source:** `= this.source` (`= this.source-type`)
