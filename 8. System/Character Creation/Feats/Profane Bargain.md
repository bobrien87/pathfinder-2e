---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "18"
traits: ["[[Divine]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can strike a profane bargain with a willing, sapient creature. That creature promises to never take hostile actions against you, to never lie to you, to never speak of this bargain, and to either perform, or refrain from performing, one other specified task, such as paying you a specified sum every year, gifting you their first-born child, or never speaking.

If the target accepts, they verbally make a request. You can choose to twist their request by selecting specific details, as long as you still fulfill the requirements of their request. If the request could be granted by a [[Wish]] ritual, you spend 1 Mythic Point and the request is magically granted.

As long as the bargain persists, you always know the target's location, can communicate telepathically with the target at any distance, and can see through the target's senses by taking a single action that has the concentrate trait. Once per day, you can take control of the target as an activity that takes three actions and has the concentrate trait. When you do, they become [[Controlled]] by you for 10 minutes. They have no memory of their time spent under your control.

If the target ever breaks the terms of this bargain, you immediately select one of the following punishments: they die, they die and you possess their soul, they become permanently controlled by you, or they become imprisoned in a cell within your realm's dungeon (you must have the [[Imprison Foe]] feat to select this final option).

A target can only enter into a Profane Bargain with you once—not even the breaking of this bargain, death, a *wish* ritual, or divine intervention frees them of this limitation. You can't make a Profane Bargain with yourself.

**Source:** `= this.source` (`= this.source-type`)
