---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whenever you Cast a Spell that requires more than one action to cast, the signature Thassilonian runes you trace in the air flicker with light and command attention. They may blaze brightly, leave lingering fog, create discordant noise, or fill the air with an overwhelming scent, such that their presence obfuscates you from onlookers. You gain [[Concealment]] from enemy creatures until the beginning of your next turn. The DC to identify your spells as you cast them is 2 higher than normal.

**Source:** `= this.source` (`= this.source-type`)
