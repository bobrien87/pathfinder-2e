---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Champion]]"]
prerequisites: "exalted reaction"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You improve your exalted reaction with the benefit listed for your cause.

**Desecration** While you have the benefit, you also gain a +2 status bonus to saving throws against effects created by enemies in your champion's aura.

**Grandeur** Any *revealing light* created by your [[Flash of Grandeur]] lasts for 1 minute.

**Iniquity** The damage dealt to enemies other than the triggering creatures increases by an amount equal to the damage dice of [[Destructive Vengeance]] (apply this after you halve the damage).

**Justice** The penalty is –2 instead of –5.

**Liberation** You and all affected allies can attempt to break free, not just the triggering ally.

**Obedience** The damage dealt to creatures other than the triggering creature who refuse to drop [[Prone]] increases to half the damage the triggering creature would take (roll the damage only once for all affected creatures).

**Redemption** The resistance isn't reduced.

**Source:** `= this.source` (`= this.source-type`)
