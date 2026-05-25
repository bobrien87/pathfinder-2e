---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Martial Artist|Martial Artist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Martial Artist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a missed Strike with a melee unarmed attack.

You have trained rigorously to use all parts of your body as a weapon, and when you miss with an attack, you can usually continue the attack with a different body part and still deal damage. Make another Strike with a melee unarmed attack, using the same multiple attack penalty as the missed Strike, if any.

**Source:** `= this.source` (`= this.source-type`)
