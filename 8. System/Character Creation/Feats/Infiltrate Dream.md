---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sleepwalker|Sleepwalker]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Mental]]", "[[Occult]]"]
prerequisites: "Sleepwalker Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Entering a dream is as natural to you as stepping through a doorway. If you're adjacent to a sleeping creature, you can enter a lucid dreamlike state, a process taking 10 minutes, to mentally walk into their dreamscape. While in the target's dream, you witness its contents, plots, and emotional experiences as an observer, though nothing within the dream can perceive or interact with you. Your target becomes temporarily immune to Infiltrate Dream for 1 week. You can't enter the dreams of a creature that doesn't have a conscious mind or doesn't dream.

While within the dream, you can attempt an [[Occultism]] check against the target's Will DC to interpret symbolism and learn information about a single topic. If the target has no knowledge of the topic, you learn they don't know about the topic unless your result is a critical failure.
- **Critical Success** You learn a piece of information directly relevant to the topic unless the target would want to hide it. If so, you learn something related to the topic but not a direct answer.
- **Success** You receive a hint or clue about the topic. This clue won't be inaccurate, but it's cryptic, vague, or might be understandable only with additional information.
- **Critical Failure** The dreams mislead you, and you learn an erroneous piece of information.

**Source:** `= this.source` (`= this.source-type`)
