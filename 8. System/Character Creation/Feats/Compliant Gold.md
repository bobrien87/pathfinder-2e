---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a melee weapon ikon

You can command your weapon to shrink or grow, for convenience or power. Even when your ikon is not empowered, you can shrink it to a miniature size (with negligible Bulk) and keep it tucked behind an ear, in your hair, or in a similar discreet location. You can shrink your weapon or regrow it to its normal size as part of drawing it, putting it away, swapping it, or picking it up.

**Immanence** Your ikon gains the reach trait. If it already had the reach trait, it instead increases your reach by an additional 10 feet, instead of the usual additional 5 feet.

**Transcendence—[[Topple the Pillar of Heaven]]** `pf2:2` (transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.Ypwa9HIw7uXdt25D inline]

**Source:** `= this.source` (`= this.source-type`)
