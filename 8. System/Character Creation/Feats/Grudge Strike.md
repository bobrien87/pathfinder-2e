---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your attuned apparition grants Heraldry Lore or Underworld Lore as an apparition skill.

You channel the spiritual power of spiteful grudges. Make a melee Strike against a creature within your reach. You gain a +2 circumstance bonus to your attack roll and deal an additional 2d6 void damage to the target; if the target is undead or otherwise has void healing, this Strike instead deals an additional 2d6 vitality damage. This ability gains the vitality trait if it deals vitality damage, or the void trait if it deals void damage.

**Source:** `= this.source` (`= this.source-type`)
