---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "armor, construct, or weapon innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin

Taking inspiration from Desna's image as a giant silk moth in Tian Xia, you've attached a bracelet to your innovation that generates ultra-strong silk strands mixed with venom. You can unleash this substance as part of an attack. Make a melee Strike. If it hits, the target takes damage from the Strike as normal and must attempt a [[Fortitude]] save against your class DC with the following effects.
- **Critical Success** The target is unaffected.
- **Success** The silk imposes a –10 foot status penalty to all the target's Speeds for 1 round.

> [!danger] Effect: Silk Bracelet
- **Failure** As success, and the target takes an additional @Damage[(floor(@actor.level/6))d4[persistent,poison]] damage. The poison damage increases to 2d4 at 12th level and 3d4 at 18th level.
- **Critical Failure** As failure, and the target is [[Immobilized]] until the end of their next turn.

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
