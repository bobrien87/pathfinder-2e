---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]"]
prerequisites: "trained in Deception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enter a seemingly unfocused stance that mimics the movements of the inebriated-bobbing, weaving, leaving false openings, and distracting your enemies from your true movements.

While in this stance, you gain a +1 circumstance bonus to Deception checks to [[Feint]]. The only Strikes you can make are stumbling swing unarmed attacks. These deal 1d8 bludgeoning damage; are in the brawling group; and have the agile, backstabber, finesse, nonlethal, and unarmed traits.

If an enemy hits you with a melee Strike while in this stance, it becomes [[Off Guard]] against the next stumbling swing Strike you make against it before the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
