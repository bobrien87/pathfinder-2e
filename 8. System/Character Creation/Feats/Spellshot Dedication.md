---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spellshot|Spellshot]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "way of the spellshot"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cast arcane spells like a wizard, gaining a spellbook with four common arcane cantrips of your choice. You gain the Cast a Spell activity. You can prepare two cantrips each day from your spellbook. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for spellshot archetype spells is Intelligence, and they are arcane spells. You become trained in Arcana; if you were already trained in Arcana, you instead become trained in a skill of your choice. This feat counts as [[Wizard Dedication]] for the prerequisites of [[Basic Wizard Spellcasting]].

**Special** You can't select another dedication feat other than [[Beast Gunner Dedication]] until you've gained two other feats from the Spellshot or Beast Gunner archetypes.

**Source:** `= this.source` (`= this.source-type`)
