---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Fighter]]", "[[Press]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a finesse weapon or polearm.

While your opponent is still recovering from your prior attack, you snag its armor, clothing, or flesh to move it as you please. Make a melee Strike with a finesse weapon or polearm. If you hit a target that is your size or smaller, you can automatically [[Reposition]] it, with the same benefits as the Reposition action (including the critical success effect, if your Strike was a critical hit). If you used a weapon with reach, use the weapon's reach for this Reposition. If you're wielding a polearm, you can ignore Reposition's requirement that you have a hand free.

This Strike has the following failure effect.
- **Failure** The target becomes [[Off Guard]] until the end of your current turn.

**Source:** `= this.source` (`= this.source-type`)
