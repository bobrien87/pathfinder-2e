---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Champion]]"]
prerequisites: "blessed shield, champion's reaction, Shield Warden"
frequency: "once per round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Trigger** An enemy's attack against an ally matches the trigger for both your Shield Block reaction and your champion's reaction.

When you shield your ally against an attack, you call upon your power to protect your ally further. You use the Shield Block reaction to prevent damage to an ally and also use your champion's reaction against the enemy that attacked your ally.

**Special** If you have an ability that gives you an additional reaction you can use to Shield Block or use your champion's reaction, you can use it for Shield of Reckoning.

**Source:** `= this.source` (`= this.source-type`)
