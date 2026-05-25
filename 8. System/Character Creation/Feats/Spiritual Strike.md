---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scions Of Domora|Scions Of Domora]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Scion of Domora Dedication"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a weapon with at least one fundamental rune and your familiar is adjacent to you or in your space.

Your spirit guide enhances your attacks with occult power. Make a Strike with a weapon that has at least one fundamental rune. This counts as two attacks when calculating your multiple attack penalty. The Strike has the effects of the ghost touch property rune and deals an additional 2d6 force damage. If your weapon has a major striking rune, this Strike instead deals 3d6 force damage.

**Source:** `= this.source` (`= this.source-type`)
