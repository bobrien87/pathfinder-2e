---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm or loaded crossbow in one hand and a bludgeoning or slashing melee weapon in the other.

You hurl your melee weapon at an opponent, then fire a bullet into the weapon's hilt, making it bounce back to your grasp. Make a thrown ranged Strike with the melee weapon, then a ranged Strike with your firearm. This counts as two attacks for your multiple attack penalty, but you don't apply the penalty until after you've completed both attacks. If the melee weapon doesn't already have the thrown trait, it gains the thrown 10 feet trait during a Rebounding Assault.

If both attacks are successful, the bolt or bullet hits the thrown melee weapon instead of your target, adding its force into one attack. Combine the damage from both Strikes, using the thrown weapon's damage type, and add an additional 1d6 precision damage. The impact sends the melee weapon rebounding off the target and back to your hand.

In any circumstance other than both attacks hitting, carry out the individual Strikes normally. The thrown weapon doesn't rebound and remains in the target's space as normal for thrown weapons.

**Source:** `= this.source` (`= this.source-type`)
