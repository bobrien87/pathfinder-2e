---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "18"
traits: ["[[Healing]]", "[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The servants of apocalypse know that it is impossible to cheat death, but your will is sufficient to help you outlive even your strongest enemies. The first time each day you would be reduced to 0 Hit Points but not immediately killed, you avoid being knocked out and instead of taking the damage, you regain a number of Hit Points equal to @Damage[(2*@actor.level)[healing]]{twice your level}. Your [[Wounded]] condition increases by 1.

In addition, whenever you have the wounded condition, you gain a status bonus to your Armor Class equal to your wounded condition value and a status bonus to the damage of your Strikes equal to twice your wounded condition value.

**Source:** `= this.source` (`= this.source-type`)
