---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophet Of Kalistrade|Prophet Of Kalistrade]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Mercantile Lore and Society, Charisma +2"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Druma

After induction into the ranks of the Kalistocrats, you learned the skills necessary to succeed in business and rise above others by following a set of detailed strictures. Unless you take measures to hide your affiliation, anyone who has heard of the Prophets of Kalistrade will know you're one of them when they see you. You become an expert in Society and can use Society instead of Diplomacy to [[Make an Impression]] on merchants and traders.

Additionally, if you don't already cast spells from spell slots, you learn to cast spontaneous spells and gain the Cast a Spell activity. You gain a spell repertoire with two common occult cantrips, plus either  or [[Read Aura]]. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for these spells is Charisma, and they're occult spells.

Prophet of Kalistrade

**Source:** `= this.source` (`= this.source-type`)
