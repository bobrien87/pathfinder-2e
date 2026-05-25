---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Emissary|Rivethun Emissary]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Diplomacy and Religion"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Followers of Rivethun have access to this feat.

You're a practicing Rivethun emissary, skilled at interacting and bonding with the spirits of living creatures. You become an expert in Diplomacy and Religion. You also gain the [[Bond with Spirit]] activity and the [[Entreat Spirit]] focus spell. If you don't already have one, you gain a focus pool, which you can regain using the Refocus activity to nurture your personal well of spiritual power. Your Rivethun focus spells are divine spells; when you gain this feat, you become trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for Rivethun focus spells is Wisdom.

Rivethun Emissary

**Source:** `= this.source` (`= this.source-type`)
