---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The call of a long dead runelord has infected your soul and transformed your fate. Choose one of the following sins: envy, gluttony, greed, sloth, or wrath. You become trained in Arcana. If you are already trained in Arcana, you become trained in the skill of your choice. At 14th level, you gain expert proficiency in Arcana. At 16th level, if you gain master proficiency in Arcana.

You have familiarity with weapons in the polearm and spear weapon groups—for the purposes of proficiency, you treat any of these that are martial weapons as simple weapons and any that are advanced weapons as martial weapons. You learn the Thassilonian language.

You gain the ability to cast an arcane spell as an innate spell. This spell must be chosen from the following list: [[Darkvision]], [[Mystic Armor]], [[Runic Body]], [[Runic Weapon]], [[See the Unseen]], [[Sending]], or [[Truesight]]; alternatively, you can choose any spell of 6th rank or lower from the sin spells listed for your chosen sin. You can cast this spell as an arcane innate spell once per day. The spell is automatically heightened to a spell rank equal to half your level rounded up. Use mythic proficiency to determine any attack rolls or spell DCs.

Your obsession with revenge allows you to reflexively lash out at those who harm you with blasts of arcane magic. You gain the [[Runelord's Response]] reaction.

Avenging Runelord (Rare)

**Source:** `= this.source` (`= this.source-type`)
