---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eldritch Archer|Eldritch Archer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Magical]]"]
prerequisites: "expert in at least one weapon from the bow or crossbow weapon group"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You channel powerful magic with your archery, allowing you to deliver potent spells through the tip of an arrow rather than the more mundane flick of the wrist or whatever other gestures are usually used.

If you don't already cast spells from spell slots, you learn to cast spontaneous spells and gain the Cast a Spell activity. You gain a spell repertoire with one cantrip of your choice, from a tradition of your choice. You choose a common cantrip or other cantrip to which you have access. This cantrip must require a spell attack roll and come from your chosen tradition. You're trained in spell attack modifier and spell DC. Your key spellcasting attribute for these spells is Charisma. Regardless of whether you can already cast spells or gained the ability from this dedication, you gain the [[Eldritch Shot]] activity.

Eldritch Archer

**Source:** `= this.source` (`= this.source-type`)
