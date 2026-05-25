---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fighter]]", "[[Press]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a melee weapon in two hands.

Your final blow can make an impact even if it rebounds off a foe's defenses. Make a Strike with a melee weapon you're wielding in two hands. After the Strike, your turn ends. The Strike deals one additional weapon damage die, or two additional weapon damage dice if you're at least 18th level. The Strike also gains the following failure effect.
- **Failure** You deal damage equal to one weapon damage die of the required weapon. Increase this to two dice if you're at least 18th level.

**Source:** `= this.source` (`= this.source-type`)
