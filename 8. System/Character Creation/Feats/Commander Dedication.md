---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Commander|Commander]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Intelligence +2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the tactics class feature like a commander and gain your own folio; this folio contains two common mobility or offensive tactics of your choosing. You can prepare one of these tactics whenever a commander would be able to prepare tactics. You gain a commander's banner that grants you a 30-foot aura for the purposes of using your tactics, but the banner does not grant the commander's banner bonus to Will saves and DCs against fear effects. You become trained in commander class DC and Warfare Lore; if you were already trained in Warfare Lore, you become trained in another Lore skill of your choice.

Commander

**Source:** `= this.source` (`= this.source-type`)
