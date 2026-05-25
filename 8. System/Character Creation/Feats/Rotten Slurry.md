---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Deviant]]", "[[Magical]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You expel a glob of rotten, foul-smelling slurry from your torso, hand, or mouth at a foe. Make a ranged Deviant check{attack roll} against a creature within 30 feet. If you succeed, the slurry deals @Damage[(floor(@actor.level/2)d4)[bludgeoning]] damage to the target for every two levels you have, or double damage on a critical success. A creature that's damaged by the attack is [[Sickened]] 1 ([[Sickened]] 2 on a critical success).

**Awakening** The slurry bursts, showering bystanders. The attack deals an additional @Damage[((floor(@actor.level/4)d4)[splash])[poison]]{1d4 poison splash} damage for every four levels you have.

**Awakening** The slurry is caustic, and bores into the flesh of those it touches. The attack deals an additional 1d4 persistent,acid damage.

**Source:** `= this.source` (`= this.source-type`)
