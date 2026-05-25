---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Nephilim]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spilled blood is sanctified, with effects similar to those of [[Holy Water]]. Whenever a fiend, undead, or creature with a weakness to holy drinks your blood or deals piercing or slashing damage to you with jaws, fangs, or a similar attack, that creature takes @Damage[1d6[spirit]|traits:holy] damage with the holy trait. You gain a +4 circumstance bonus to Crafting checks to [[Craft]] *holy water* using your blood as one of the ingredients.

**Source:** `= this.source` (`= this.source-type`)
