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

**Usage** imbued into a body ikon or worn ikon

Small wings, flaming wheels, or another signifier of flight sprout from your ikon as it gains the power to lift you from the ground. Your ikon gains the following effects.

**Immanence** Your ikon keeps you hovering even without conscious effort. You can remain in the air at the end of this turn, even if you didn't use a Fly action.

**Transcendence—[[Race the Skies]]** `pf2:1` (concentrate, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.MrTULCUsE9naPxXg inline]

**Source:** `= this.source` (`= this.source-type`)
