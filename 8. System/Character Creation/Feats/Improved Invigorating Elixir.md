---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Alchemist]]"]
prerequisites: "Invigorating Elixir"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Choose physical invigoration or mental invigoration, and add the listed conditions to those you can choose for an invigorating elixir you create to counteract:

**Physical Invigoration** [[Blinded]], [[Deafened]], [[Drained]], [[Paralyzed]], [[Slowed]]

**Mental Invigoration** [[Confused]], controlled, [[Fleeing]], [[Frightened]], [[Paralyzed]], [[Slowed]].

**Special** You can select this feat a second time to choose a different type of invigoration and add its options to those you can choose.

**Source:** `= this.source` (`= this.source-type`)
