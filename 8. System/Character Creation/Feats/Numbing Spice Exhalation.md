---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Additive]]", "[[Alchemist]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can mix alchemically preserved peppers into an alchemical food consumable to spice it up with alchemical fire. When the modified alchemical food is consumed, the user's mouth goes numb temporarily. Once within the next hour, they can spend a single action to breathe a gout of flame in a @Template[type:cone|distance:15]. Each creature in the cone takes @Damage[(floor(@actor.level/2))d6[fire]|options:area-damage]{1d6 fire damage for every two levels you have} with a [[Reflex]] save against your class DC.

**Source:** `= this.source` (`= this.source-type`)
