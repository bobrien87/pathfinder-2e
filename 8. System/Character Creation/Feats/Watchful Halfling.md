---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Halfling]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You pay close attention to the people around you, allowing you to more easily notice when they act out of character. You gain a +2 circumstance bonus to Perception checks when using the [[Sense Motive]] basic action to notice enchanted or possessed characters. If you aren't actively using Sense Motive on an enchanted or possessed character, the GM rolls a secret check, without your usual circumstance bonus, for you to potentially notice the enchantment or possession anyway.

In addition to using it for skill checks, you can use the [[Aid]] basic action to grant a bonus to another creature's saving throw or other check to overcome enchantment or possession. As usual for Aid, you need to prepare by using an action on your turn to encourage the creature to fight against the effect.

**Source:** `= this.source` (`= this.source-type`)
