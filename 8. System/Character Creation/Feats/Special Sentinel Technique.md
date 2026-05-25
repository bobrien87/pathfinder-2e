---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starlit Sentinel|Starlit Sentinel]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Starlit Sentinel Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can channel the power of your constellation into a unique technique. You gain either the [[Luminous Stardust Healing]] or [[Shining Starlight Attack]] focus spell, which you can cast only in sentinel form. When you gain this feat, decide a name for your technique, which becomes the spell's incantation.

If you don't already have one, you gain a focus pool of 1 Focus Point, which you can Refocus by spending 10 minutes outside of your sentinel form to reflect on the values of your constellation. Starlit sentinel focus spells are arcane spells. You become trained in spell attack modifier and spell DC, and your spellcasting ability for these spells is Charisma.

**Special** You can take this feat a second time, gaining the focus spell that you didn't gain the first time.

**Source:** `= this.source` (`= this.source-type`)
