---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into the Mirror Aegis

You stole a gorgon's gaze and trapped it in your ikon. You've learned how to brandish it for your advantage, subduing the rage of the trapped gaze by turning it on your enemies.

**Transcendence—[[Brandish the Gorgon's Gaze]]** `pf2:1` (earth, transcendence, visual)

@Embed[Compendium.pf2e.actionspf2e.Item.5VbPhxZYfagIqE1z inline]

**Source:** `= this.source` (`= this.source-type`)
