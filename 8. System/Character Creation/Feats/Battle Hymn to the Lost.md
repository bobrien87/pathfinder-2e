---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]"]
prerequisites: "of verse unbroken or peerless under heaven"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Your movements in combat are an artistic dirge to those spirits who could not fight to see another day. You make a Strike. Regardless of whether the Strike succeeds, spirits of warriors who died gloriously in battle surge out to attack with you. They appear in a @Template[type:cone|distance:30] if you make a melee Strike or in a @Template[type:emanation|distance:10] around your target if you made a ranged Strike. Each enemy in the area takes @Damage[(floor(@actor.level/4))d10[untyped]|options:area-damage|shortLabel] damage with a [[Reflex]] save against your class DC; you choose whether the damage is bludgeoning, piercing, or slashing. At 12th level and every 4 levels thereafter, the damage increases by 1d10.

As they join the battle, the spirits call your fallen allies back to the fight. Any of your allies in the area who are [[Dying]] regain Hit Points equal to the damage you rolled. This is a divine, healing, vitality effect.

**Source:** `= this.source` (`= this.source-type`)
