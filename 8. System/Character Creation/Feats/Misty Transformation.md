---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Druid]]", "[[Primal]]"]
frequency: "once per PT1M"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Trigger** You transform due to a polymorph effect. Wild mists cover your form.

You create a hazy cloud in a @Template[burst|distance:5] centered on one corner of your space. If your new form is Large or larger, the cloud covers your entire space instead. All creatures within the area are [[Concealed]], and all others are concealed to them. The cloud lasts until the beginning of your next turn but is immediately dispersed by a strong wind.

**Source:** `= this.source` (`= this.source-type`)
