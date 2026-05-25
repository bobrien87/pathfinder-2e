---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Involutionist|Rivethun Involutionist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature and Religion"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Followers of Rivethun have access to this feat.

You're a practicing Rivethun involutionist, with a deep well of inner power. You become an expert in Nature and Religion. You cast spells and gain the Cast a Spell activity. You gain a spell repertoire with two common cantrips from the divine spell list or any other divine cantrips you've learned or discovered. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for Rivethun involutionist archetype spells is Wisdom.

Rivethun Involutionist

**Source:** `= this.source` (`= this.source-type`)
