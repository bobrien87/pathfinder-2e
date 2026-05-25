---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Animist|Animist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Wisdom +2"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have formed a bond with an apparition and can cast divine spells. Choose a single apparition from those available to the animist. You become bound to that apparition and can attune to it each day during your daily preparations to become trained in its apparition skills. If you are 8th level, you are expert in its apparition skills while attuned to it, and if you are 16th level, you are a master in its apparition skills while attuned to it. You can spend 1 day of downtime ending your relationship with this apparition and bonding to a new one.

You gain the Cast a Spell activity. You can prepare two common cantrips each day from the divine spell list or any other divine cantrips you have access to, including the cantrip listed in your apparition's apparition spells. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for animist archetype spells is Wisdom, and they are divine animist spells.

Animist

**Source:** `= this.source` (`= this.source-type`)
