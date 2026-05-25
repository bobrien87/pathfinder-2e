---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your mount has a supernatural hunger for mortal souls that you can feed. Once per day, you can cast [[Seize Soul]] as a divine innate spell. The spell gains a cost of 1 Mythic Point but you can use your apocalypse mount as the item in which you store the soul. Your apocalypse mount counts as an artifact for the purpose of the spell. At any point while your apocalypse mount contains a soul, you can Sustain the spell to allow your apocalypse mount to consume the soul. It regains a number of Hit Points equal to @Damage[(2*@actor.level)[healing]]{twice your level}. For the next minute, it also gains a +20-foot status bonus to its Speed and its unarmed attack Strikes are made at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
