---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bard|Bard]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Charisma +2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cast spells like a bard and gain the Cast a Spell activity. You gain a spell repertoire with two common cantrips from the occult spell list or any other occult cantrips you've learned or discovered. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for bard archetype spells is Charisma, and they are occult bard spells. You become trained in Occultism and Performance; for each of these skills in which you were already trained, you instead become trained in a skill of your choice. Choose a muse as you would if you were a bard. You can take that muse's feats, but you don't gain the starting feat, spell or any other abilities the choice of muse grants.

Bard

**Source:** `= this.source` (`= this.source-type`)
