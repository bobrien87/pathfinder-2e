---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a worn ikon

Your ikon gains a pin, stripe, or similar marking showing you as a master of your craft. The imbued ikon gains the following ability.

**Transcendence—[[A Challenge for Heroes]]** `pf2:2` (concentrate, mental, spirit, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.c40APnn4a7bWhtcZ inline]

**Source:** `= this.source` (`= this.source-type`)
