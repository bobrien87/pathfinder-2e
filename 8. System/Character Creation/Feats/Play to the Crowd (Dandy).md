---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Dandy Dedication, master in Deception"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a knack for knowing just how to manipulate groups by saying exactly what needs to be said. When you [[Lie]] in a public area in front of a crowd, you can gauge the reactions of the crowd as you speak to know how your Lie is working, and Lie loses its secret trait. You gain the [[Reactive Falsehood]] reaction.

**Source:** `= this.source` (`= this.source-type`)
