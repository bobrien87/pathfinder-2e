---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Winged Warrior|Winged Warrior]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Winged Warrior Dedication"
frequency: "once per PT1H"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Unfurling your wings in a quick snap, you send feathers scattering in all directions. Creatures in a @Template[emanation|distance:15] take @Damage[6d6[slashing]|options:area-damage] damage ([[Reflex]] save against your class DC). This increases to @Damage[10d6[slashing]|options:area-damage] if your unarmed attacks have a greater striking rune, such as by etching it onto [[Handwraps of Mighty Blows]], and @Damage[16d6[slashing]|options:area-damage] if they have a major striking rune.

**Source:** `= this.source` (`= this.source-type`)
