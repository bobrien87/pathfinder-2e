---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Swashbuckler]]"]
prerequisites: "Opportune Riposte"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ripostes can deflect attacks back at their source. You can use [[Opportune Riposte]] with a trigger of "A foe outside of your reach critically fails an attack roll against you" in addition to its usual trigger.

When you use Opportune Riposte with this new trigger against a ranged attack, your Strike deflects some of the triggering effect back toward its source. Compare the result of your attack roll to the AC of the triggering foe.

On a hit, you deal the normal amount of damage for your Strike, but the damage type changes to that of the triggering attack. For instance, if you used Opportune Riposte to deflect a [[Blazing Bolt]], your Strike would deal fire damage instead of its normal damage type.

**Source:** `= this.source` (`= this.source-type`)
