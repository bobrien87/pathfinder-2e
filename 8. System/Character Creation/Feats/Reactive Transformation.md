---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Druid]]"]
prerequisites: "Untamed Form, Dragon Shape, Elemental Shape, Plant Shape, or Soaring Shape"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** varies

You transform reflexively when in danger. You cast [[Untamed Form]] to transform into one shape granted by one of the prerequisite feats you have, depending on the trigger. Your shape's resistances and weaknesses apply against the triggering damage.

**Trigger** You fall 10 feet or more

**Effect** Choose a shape from [[Aerial Form]].

**Trigger** You take bludgeoning or poison damage

**Effect** Choose a primal dragon shape from [[Dragon Form]] that resists the triggering damage.

**Trigger** You take fire damage

**Effect** Choose a fire elemental shape from [[Elemental Form]].

**Trigger** You take poison damage

**Effect** Choose a shape from [[Plant Form]].

**Source:** `= this.source` (`= this.source-type`)
