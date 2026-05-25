---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Monk]]"]
prerequisites: "expert in Deception, Stumbling Stance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Stumbling Stance]].

You lash out confusingly with what seems to be a weak move but instead allows you to unleash a dangerous flurry of blows upon your unsuspecting foe.

When you use [[Flurry of Blows]], you can attempt a check to [[Feint]] as a free action just before the first Strike.

On a success, instead of making the target [[Off Guard]] against your next attack, they become off-guard against both attacks from the Flurry of Blows.

**Source:** `= this.source` (`= this.source-type`)
