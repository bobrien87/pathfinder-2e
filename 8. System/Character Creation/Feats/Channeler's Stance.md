---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Stance]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enter a stance that allows power to flow through you. While in this stance, whenever you cast or Sustain an apparition spell or vessel spell that deals energy damage, you gain a status bonus to the spell's damage equal to the spell's rank.

Each time you Cast a Spell that has the vitality or void traits and that restores Hit Points while in this stance, the spells' targets gain a status bonus to the initial amount of healing received equal to the spell's rank. This bonus healing does not apply to healing over time effects (such as fast healing or regeneration).

**Source:** `= this.source` (`= this.source-type`)
