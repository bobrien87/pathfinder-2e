---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Exemplar]]", "[[Ikon]]", "[[Morph]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a body or worn ikon

Rage courses through your body, transforming you into a beast of battle. The imbued ikon gains the following abilities.

**Immanence** You're affected by a 4th-rank [[Enlarge]] spell. You can choose to forgo this effect when your body ikon becomes empowered.

**Transcendence—[[Spasm of the Berserker]]** `pf2:1` (transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.tHHpBREXDaafK3TF inline]

**Source:** `= this.source` (`= this.source-type`)
