---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Animist]]", "[[Apparition]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your attuned apparition grants Forest Lore or Ocean Lore as one of its apparition skills.

Your apparitions share with you the monstrous nature of those creatures who dwell in deep seas or ancient woods. You add [[Monstrosity Form]] to your apparition spell repertoire, allowing you to cast it with your apparition spellcasting.

**Special** If you are attuned to a stalker in darkened boughs, add the phoenix form from *monstrosity form* to your available [[Darkened Forest Form]] options when you cast the spell heightened to 8th rank.

If you are attuned to a lurker in devouring dark, add the cave worm and sea serpent forms to your [[Devouring Dark Form]] options as a polymorph effect when you cast the spell heightened to 8th rank.

**Source:** `= this.source` (`= this.source-type`)
