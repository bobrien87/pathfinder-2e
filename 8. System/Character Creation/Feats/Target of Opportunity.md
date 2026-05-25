---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Manipulate]]"]
prerequisites: "Marshal Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally succeeds at a ranged Strike against an opponent in your weapon's first range increment.

**Requirements** You have a ranged or thrown weapon in hand.

You capitalize on your ally's attack and use the opportunity to secure a blow of your own, adding to the oncoming barrage. Make a ranged Strike with a –2 penalty against the opponent targeted by the triggering attack. This Strike doesn't count toward your multiple attack penalty, and your multiple attack penalty doesn't apply to this Strike. If this Strike is successful, combine the damage from the attack with the damage from your ally's attack for the purpose of resistances and weaknesses.

**Source:** `= this.source` (`= this.source-type`)
