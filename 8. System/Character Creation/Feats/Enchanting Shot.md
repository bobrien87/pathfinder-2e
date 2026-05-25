---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eldritch Archer|Eldritch Archer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Magical]]", "[[Mental]]"]
prerequisites: "Eldritch Archer Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a single whisper carried on the wind, you enchant your ammunition to make a foe more vulnerable to your attacks.

Make a bow or crossbow Strike. On a hit, the target takes an additional 2d6 mental damage. On a critical hit, the target also becomes [[Stunned]] 1. The mental damage increases to 3d6 if your weapon has a *greater striking rune*, or to 4d6 if your weapon has a *major striking rune*.

**Source:** `= this.source` (`= this.source-type`)
