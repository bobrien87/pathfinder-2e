---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued in one or two weapon ikons that both have the thrown trait (see text)

Your ikons bond like a pair of one-winged birds. This feat can be imbued in either a single ikon with multiple copies, such as one produced by the [[Shadow Sheath]] or with the [[Twin Stars]] feat, or two separate ikons (bypassing the normal limit per ikon feat).

**Immanence** As long as you hold one ikon, the other will return to find its partner. Both ikons gain the returning rune.

**Transcendence—[[Rejoin in Flight]]** `pf2:2` (transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.I08t3hnpMZSRX5Ug inline]

**Source:** `= this.source` (`= this.source-type`)
