---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication, hero-god accomplishment"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As word of your faith spreads, so too does word of your foibles and weaknesses. Where originally these disadvantages may have been myths themselves, or simply manifestations of ill fortune or chance, when you take this feat, one of those weaknesses becomes real.

Work with your GM to choose your heroic weakness—it must be to a specific damage type and must be associated with a specific condition, both of which must be elements that are going to be significant parts of your story's future. For example, you could choose for a weakness to be spirit damage caused to you by a follower of a rival god, physical damage from a specific category of weapon, void damage caused by a specific kind of undead, or fire damage taken in a certain part of the world or from creatures from that part of the world. The amount of weakness you gain to this damage is equal to twice your level.

But with this new weakness comes a new source of power, for when your foes would take advantage of your weakness, you can use the pain and humiliation to bolster your own resolve. You gain the [[Makes Me Stronger]] reaction.

**Source:** `= this.source` (`= this.source-type`)
