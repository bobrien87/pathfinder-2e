---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Arcana, Nature, Occultism, or Religion"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Learning spells comes easily to you. When you succeed at Learning a Spell, it takes 10 minutes regardless of the spell's rank. If you would succeed on the check, you critically succeed instead. If you fail, you can try again after a week or after you gain a level, whichever is first.

You can use downtime to learn and inscribe new spells. This works as if you were using [[Earn Income]] with the tradition's associated skill, but instead of gaining money, you choose a spell available to you to learn and gain a discount on learning it, learning it for free if your earned income equals or exceeds its cost.

**Source:** `= this.source` (`= this.source-type`)
