---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Five Breath Vanguard|Five Breath Vanguard]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]"]
prerequisites: "Induce Imbalance"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** You're in an elemental stance, and the target is under the effects of Induce Imbalance.

You cycle through the elements in a devastating combination attack. Strike the target using the unarmed attack associated with your current elemental stance, then [[Cycle Elemental Stance]]. Then, Strike the target with the unarmed attack associated with your new elemental stance. You can continue to Cycle Elemental Stance and Strike until you've made a Strike using the unarmed attack of every elemental stance you know, applying the multiple attack penalty as usual. If you successfully hit the target with all five elemental Strikes using this ability, it must attempt a [[Fortitude]] save against your class DC or die as each elementally associated organ within its body shuts down; this is a death effect.

**Source:** `= this.source` (`= this.source-type`)
