---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Auditory]]", "[[Hobgoblin]]", "[[Manipulate]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** An adjacent and willing ally would be reduced to 0 HP but not killed.

You physically help an ally remain standing and encourage them to push through their pain against dire odds. Your ally doesn't fall [[Unconscious]] and remains at 1 Hit Point. The ally also gains a number of temporary Hit Points equal to your level that last for 1 minute. Fighting onward with such an injury isn't without consequence; your ally's [[Wounded]] condition increases by 1.

> [!danger] Effect: Can't Fall Here

**Source:** `= this.source` (`= this.source-type`)
