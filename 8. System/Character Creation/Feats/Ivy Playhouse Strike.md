---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Dandy Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've spent so many hours at the Ivy Playhouse or sparring with the Street Performers and Actors' Guild that you've picked up some stage combat techniques. In a fight, you can apply these approaches to make an attack less harmful but more confounding to your foes. Make a melee Strike. If you hit, you take a circumstance penalty to damage equal to the number of weapon damage dice, and the damage gains the nonlethal trait. However, the target is perplexed by the theatricality of your attack and becomes [[Clumsy]] 1 until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
