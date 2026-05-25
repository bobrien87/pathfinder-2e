---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ursine Avenger Hood|Ursine Avenger Hood]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Primal]]", "[[Summon]]"]
frequency: "once per PT1H"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You can cast a 3rd-rank [[Summon Animal]] as an innate spell, but only to summon a [[Black Bear]]. At 10th level, the *summon animal* spell is heightened to 4th level, and you can summon a [[Grizzly Bear]]. At 12th level, your *summon animal* innate spell is heightened to 5th level, and you can summon a [[Polar Bear]]. At 14th level, it's heightened to 6th level, and you can summon a [[Cave Bear]].

**Source:** `= this.source` (`= this.source-type`)
