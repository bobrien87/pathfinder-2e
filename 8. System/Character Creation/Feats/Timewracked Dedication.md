---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The current of time shifts subtly in your field of view. You have learned to tread these temporal eddies, moving forward and pushing backward in small strokes—sometimes even gaining the ability to move your allies and enemies through time as you choose. Whether or not you'll ever be fully restored to your proper timeline, you can't predict—but until then you continue to manipulate your estrangement from time to move unseen, defy your opponents in combat, and occupy future or past versions of yourself to escape distress. With practice you could gain the ability to rehearse a speech at the same tie you deliver it or attack distant foes without spending the time to move between them. Eventually, you might gain the power to vanish from existence altogether while you hop forward and backward in time or even become immortal.

Your Speed increases by 5 feet for each mode of movement available to you. You can spend a Mythic Point to roll any check made to determine your initiative at mythic proficiency. If your initiative roll result is tied with an opponent's initiative roll, you can choose to go first. In addition, you gain the [[Sidestep Through Time]] reaction.

Timewracked (Rare)

**Source:** `= this.source` (`= this.source-type`)
