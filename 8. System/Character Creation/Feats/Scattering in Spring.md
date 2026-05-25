---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Monk]]"]
prerequisites: "Twisting Petal Stance"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy within your reach targets you with a melee attack, and you're aware of the attack.

**Requirements** You're in [[Twisting Petal Stance]].

You evade an incoming attack by twisting your enemy's tactics in your favor. You gain a +2 circumstance bonus to AC against the triggering attack. If the attack misses you, you can immediately attempt a [[Feint]] or [[Shove]] against the triggering attacker; if you roll a success, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
