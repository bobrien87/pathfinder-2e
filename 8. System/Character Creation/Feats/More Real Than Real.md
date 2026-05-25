---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Shared Archetype Feats|Shared Archetype Feats]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Acrobat, Celebrity, Dandy, or Gladiator Dedication"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your performances aren't just well-known, they're famous across the land and beyond. Your ability to make people believe the stories you perform has taken on supernatural power. You gain the ability to cast [[Fabricated Truth]] once per day as an occult innate spell.

**Source:** `= this.source` (`= this.source-type`)
