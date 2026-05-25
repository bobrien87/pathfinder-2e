---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spirit Warrior|Spirit Warrior]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Spirit Warrior Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn an oath to defend the helpless from dangerous titanic beasts, including kaiju that roam the surface of Golarion. Attacks made as part of your [[Overwhelming Combination]] ability gain a +4 circumstance bonus to damage against a creature at least 2 sizes larger than you, or +6 if you have master proficiency with the weapon you used. You also gain a +2 circumstance bonus to saving throws and DCs against kaiju hazards. You gain the following edict.

**Edict** You must do everything within your power to protect others from massive creatures they can't defend themselves from; in the event the victims are evil or actively trying to harm you or other innocents, you don't have to save them.

**Source:** `= this.source` (`= this.source-type`)
