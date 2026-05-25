---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Nidalese Horselord|Nidalese Horselord]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature, horse animal companion"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Nidal.

Thanks to the deep bond you share with your Nidalese horse, the two of you gain remarkable abilities. You both gain darkvision and a +1 status bonus to saving throws against effects with the darkness or shadow trait. Your horse's Speed also increases by 5 feet.

You gain the following edicts and anathema.

**Edicts** oppose the forces of the Umbral Court where possible, provide comfort to those who suffer in darkness

**Anathema** mistreat your horse, worship Zon-Kuthon or permanently ally with those who worship Zon-Kuthon

**Special** You can pledge yourself to the cause of the Nidalese horselords if you've already taken the [[Cavalier Dedication]] feat, allowing you to take this dedication feat even if you haven't taken two additional cavalier feats.

Nidalese Horselord

**Source:** `= this.source` (`= this.source-type`)
