---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Monk]]"]
prerequisites: "expert strikes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You put all your force into a single mighty, carefully controlled blow. Make an unarmed Strike. If you spend two actions and this Strike hits, you deal an extra die of weapon damage. You can instead spend 3 actions to perform an even more powerful attack, dealing a second additional die of weapon damage on a hit.

If you're at least 10th level, the number of additional dice you add from this feat doubles, for a total of 2 additional dice if you spend 2 actions or 4 additional dice if you spend 3 actions.

If you're at least 18th level, the number of additional dice you add from this feat triples, for a total of 3 additional dice if you spend 2 actions or 6 additional dice if you spend 3 actions.

**Source:** `= this.source` (`= this.source-type`)
