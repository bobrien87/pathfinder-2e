---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Red Mantis Assassin|Red Mantis Assassin]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "trained in Religion, Red Mantis Assassin Dedication"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have learned limited divine magic from your Red Mantis training. You gain the Cast a Spell activity. You can prepare two common cantrips each day from the divine spell list or any other divine cantrips you have access to. You also gain the basic spellcasting benefits. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for the Red Mantis archetype spells is Charisma, and they are divine Red Mantis spells. If you gain a Focus Pool from any Red Mantis Assassin class feats, you can Refocus by praying to Achaekek or researching your assigned kill.

You also have access to the [[Red Mantis Magic School]]. In addition to preparing spells from the divine spell list, you can prepare spells from this school. Regardless of their usual magic tradition, when you prepare spells from this school, they are divine spells, as are any Red Mantis focus spells you gain.

**Source:** `= this.source` (`= this.source-type`)
