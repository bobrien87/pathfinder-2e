---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Psyche]]", "[[Psychic]]"]
prerequisites: "gathered lore subconscious mind"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Seeing an enemy's attack, you quickly consult multiple scraps of lore in your mind, synthesizing them into the perfect plan. Make a check to Recall Knowledge (using an appropriate skill) about one creature within 60 feet. On a success, in addition to the normal benefits, you gain a +1 circumstance bonus to your next attack roll against that creature and to your AC against the creature's next attack. On a critical success, the bonuses are +2.

**Source:** `= this.source` (`= this.source-type`)
