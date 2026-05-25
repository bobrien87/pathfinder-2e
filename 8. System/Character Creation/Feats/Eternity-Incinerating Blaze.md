---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Exemplar]]", "[[Ikon]]", "[[Void]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a weapon ikon

The blaze of your divine spark is hot enough that it burns in not just the present, but the past and future as well. Whenever you score a critical hit with the imbued ikon, the target becomes [[Doomed]] 1 or increases its doomed condition by 1. If the target's maximum dying value is reduced to 0 by this ability, it immediately dies in a flash of spiritual fire that reduces its body to ash. This effect applies even when the ikon is not empowered. The ikon also gains the following transcendence ability.

**Transcendence—[[Burn out of Time]]** `pf2:2` (spirit, transcendence, void)

@Embed[Compendium.pf2e.actionspf2e.Item.ZhVJ7EUTJngrIO2Z inline]

**Source:** `= this.source` (`= this.source-type`)
