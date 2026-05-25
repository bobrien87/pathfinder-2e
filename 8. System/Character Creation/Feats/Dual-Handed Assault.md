---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fighter]]", "[[Flourish]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a one-handed melee weapon and have a free hand.

You snap your free hand over to grip your weapon just long enough to add momentum and deliver a more powerful blow to your opponent. Make a Strike with the required weapon. You quickly switch your grip during the Strike in order to make the attack with two hands. If the weapon doesn't normally have the two-hand trait, increase its weapon damage die by one step for this attack. If the weapon has the two-hand trait, you gain the benefit of that trait and a circumstance bonus to damage equal to the weapon's number of damage dice. When the Strike is complete, you resume gripping the weapon with only one hand. This action doesn't end any stance or fighter feat effect that requires you to have one hand free.

**Source:** `= this.source` (`= this.source-type`)
