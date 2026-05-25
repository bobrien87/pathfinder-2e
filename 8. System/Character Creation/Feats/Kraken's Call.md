---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Merfolk]]", "[[Primal]]"]
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You call forth the sleeping krakens of the deep to crush your enemies. You open a dozen small portals to some lightless, watery abyss in a @Template[burst|distance:30] within 120 feet. The powerful tentacles of a kraken reach through to grab at each creature in the area. Each affected creature takes @Damage[8d6[untyped]|options:area-damage] damage depending on its [[Fortitude]] save against the higher of your class DC or spell DC. You can Sustain the call up to 1 minute. The first time you Sustain it on each subsequent turn, each creature in the area not already [[Grabbed]] by the tentacles must attempt the save.
- **Success** The creature is unaffected.
- **Failure** The creature takes full damage and is grabbed by a tentacle. A creature that's still grabbed by a tentacle at the end of its turn takes 3d6 bludgeoning damage. The tentacles' [[Escape]] DC and AC are both equal to the higher of your class DC or spell DC. A creature can attack a tentacle to attempt to free the creature trapped by it; a tentacle is destroyed if it takes 30 or more damage in a single round.
- **Critical Failure** As failure, but double damage.

**Source:** `= this.source` (`= this.source-type`)
