---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Misfortune]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would be detected by an enemy Seeking you, or an enemy would succeed at a counteract check against a spell making you [[Hidden]], [[Concealed]], or [[Undetected]].

**Requirements** Your attuned apparition grants Hunting Lore or Underworld Lore as one of its apparition skills.

Your apparition possesses a furtive and elusive nature that can influence and blend with your spiritual energy to form a protective and nearly impenetrable shroud of nondetection around you. The enemy must reroll the triggering check and take the lower result.

**Source:** `= this.source` (`= this.source-type`)
