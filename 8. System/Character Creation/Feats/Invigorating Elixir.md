---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Additive]]", "[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can mix an aromatic salve into an elixir with the healing trait to soothe physical maladies. In addition to its normal effects, the elixir can be imbibed by a creature prevented from doing so (such as a [[Sickened]] creature).

In addition to its other effects, the elixir attempts to counteract an effect imposing one of the following conditions of the imbiber's choice: [[Clumsy]], [[Enfeebled]], [[Sickened]], or [[Stupefied]]. Use half your level rounded up for the counteract rank and your class DC – 10 for the counteract modifier. The imbiber is then temporarily immune to the effects of this additive for 10 minutes. The additive can't counteract curses, diseases, or conditions that are part of the creature's normal state.

**Source:** `= this.source` (`= this.source-type`)
