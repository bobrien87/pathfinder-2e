---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Snarecrafter|Snarecrafter]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Force]]", "[[Manipulate]]"]
prerequisites: "Brastlewark Snare Engineering"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Brastlewark snarecrafters know that sometimes it's more advantageous to magically destroy a snare before it's triggered. Choose a magical snare within 120 feet that you crafted. The snare is automatically destroyed and each creature in a @Template[type:emanation|distance:5] takes @Damage[1d6[force]|options:area-damage] damage per level of the destroyed snare with a basic [[Reflex]] save against the higher of your class DC or spell DC.

**Special** If you detonate a broad snare or giant snare, choose one square that snare occupies to be the center of the emanation.

**Source:** `= this.source` (`= this.source-type`)
