---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Healing]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your turn begins.

Your wounds knit together with barely a thought. You regain @Damage[(2*@actor.level)[healing]]{Hit Points equal to double your level}. When you gain this deviation, the GM secretly selects one type of energy damage or precious material, such as fire or cold iron. When you take damage of that type, your wound smokes until the end of your next turn, preventing you from using High-Speed Regeneration.

**Awakening** Your regeneration can automatically save you from the brink of death. Once per day, you can use High-Speed Regeneration when your Hit Points would be reduced to 0 instead of the usual trigger. You avoid being knocked out and remain at the number of HP you regained.

**Awakening** Regrowth invigorates you. You gain a +10-foot status bonus to your Speed until the end of your turn.

> [!danger] Effect: High Speed Regeneration Speed Boost

**Source:** `= this.source` (`= this.source-type`)
