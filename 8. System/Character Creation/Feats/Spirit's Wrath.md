---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Attack]]", "[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
prerequisites: "spirit instinct"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You call forth an ephemeral spirit, typically the apparition of an ancestor or a nature spirit, which takes the form of a wisp. The wisp makes a melee wisp rush unarmed attack against an enemy within 120 feet of you. The wisp's attack modifier is equal to your proficiency bonus for martial weapons plus your Strength modifier plus a +2 item bonus, and it applies the same circumstance and status bonuses and penalties that you have. On a hit, the wisp deals @Damage[(4d8 + @actor.abilities.con.mod)[spirit]]{spirit damage} equal to 4d8 plus your Constitution modifier. Don't apply your Rage damage or your weapon specialization damage, but circumstance and status bonuses and penalties that would also affect the wisp's damage apply. On a critical hit, the wisp deals double damage and the target becomes [[Frightened]] 1. This attack uses and counts toward your multiple attack penalty as if you were the one attacking.

**Source:** `= this.source` (`= this.source-type`)
