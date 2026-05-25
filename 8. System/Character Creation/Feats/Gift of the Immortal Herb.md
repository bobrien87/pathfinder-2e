---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Exemplar]]", "[[Healing]]", "[[Ikon]]", "[[Light]]", "[[Vitality]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a body ikon

Your blood turns a divine gold, shining in moments its spilled and begetting new life. The imbued ikon gains the following effects.

**Immanence** If your divine spark remains in your body ikon for 10 continuous minutes, you regrow one damaged or ruined limb or organ.

**Transcendence—[[Shed the Mortal Skin]]** `pf2:1` (healing, light, transcendence, vitality)

@Embed[Compendium.pf2e.actionspf2e.Item.rU3CE5niG8vHc5x4 inline]

**Source:** `= this.source` (`= this.source-type`)
