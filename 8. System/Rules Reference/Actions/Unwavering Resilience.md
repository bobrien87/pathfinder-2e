---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a saving throw against a poison, disease, or mental effect, but you haven't rolled yet.

You tap into the power of the Plane of Wood, gaining strength and mental fortitude. You gain a +1 circumstance bonus on the triggering save. If you critically succeed at this saving throw, you become bolstered by your success; blossoms and new growth temporarily sprout all over your body, and you gain a number of temporary Hit Point equal to your level. These temporary Hit Points last for one minute. When there temporary Hit Points are lost, the verdant growth subsides.

**Source:** `= this.source` (`= this.source-type`)
