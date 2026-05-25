---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing medium or heavy armor that doesn't have the broken condition, and your current Hit Points are at half your maximum or lower.

You flex your muscles to crack your damaged armor, blasting jagged shards into nearby enemies. Each enemy in a @Template[type:emanation|distance:10] takes @Damage[(11 + max(0,(@actor.level - 14)))d6[piercing]|options:area-damage] damage with a [[Reflex]] save against your class DC. You can push any enemy that fails its save 5 feet away from you (or up to 10 feet on a critical failure). The damage increases by 1d6 per level beyond 14th.

Your armor gains the broken condition. While your armor remains broken due to Armor Break, you don't take its penalty to Speed. In addition, if the broken armor has the bulwark trait, you retain its bonus to Reflex saves, but the bonus is reduced by 1.

**Source:** `= this.source` (`= this.source-type`)
