---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Champion]]"]
prerequisites: "any feat with the oath trait"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Requirements** You can see a creature you've sworn an oath against.

You call on your oath to embolden you in combat. Select one creature you can see that you've sworn an oath against (per the terms of your oath feat). You gain a +1 status bonus to AC and saves against attacks and effects by the chosen creature. You also gain a +1 status bonus to attack rolls against the chosen creature. However, your dedication draws your focus away from all other enemies. You take a –1 status penalty to AC, attack rolls, and saves against all other creatures until you stop Enforcing your Oath.

Enforce Oath lasts indefinitely, but it ends if the enemy is reduced to 0 Hit Points, the enemy offers a legitimate surrender to you or your allies, you fall [[Unconscious]], or the enemy goes unnoticed by you for more than 1 minute. You can also Dismiss the effect as a free action.

**Source:** `= this.source` (`= this.source-type`)
