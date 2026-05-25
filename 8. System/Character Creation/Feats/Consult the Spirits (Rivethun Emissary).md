---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Emissary|Rivethun Emissary]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Exploration]]"]
prerequisites: "Rivethun Emissary Dedication"
frequency: "once per day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You spend 1 hour communing with powerful spirits of the world to gain insight, information, or advice. Select advice or answers.

If you selected advice, choose a particular goal or activity you plan to engage in today, or an event you might expect to happen today. The spirits share with you a cryptic clue or piece of advice that could help with the chosen event, often in the form of a rhyme or omen.

If you selected answers, ask two clear and concise questions. The spirits answer your questions. If the question is easy for the spirits to answer accurately, they answer clearly. Otherwise, they answer cryptically, often in the form of a rhyme or omen.

Regardless of your choice, the spirits additionally bless you, granting you a +1 status bonus with a skill that the spirits believe will be of use to you today. The GM selects this skill on behalf of the spirits. This bonus lasts until the end of the day.

> [!danger] Effect: Consult the Spirits

**Source:** `= this.source` (`= this.source-type`)
