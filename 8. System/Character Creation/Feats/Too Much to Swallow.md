---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Druid]]"]
prerequisites: "Untamed Form"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're subject to an effect you could attempt to [[Escape]].

While you might be small enough to grab normally, you can change that at a moment's notice. You cast [[Untamed Form]]. If you took on a new form that's too large for the effect, you automatically escape. Otherwise, you attempt to Escape. If this ends an effect where you entered the creature's space, such as [[Swallow Whole]], exit that creature to an adjacent area where your new form could fit.

**Source:** `= this.source` (`= this.source-type`)
