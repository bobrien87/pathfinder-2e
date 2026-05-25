---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Fire]]", "[[Inventor]]", "[[Manipulate]]", "[[Unstable]]"]
prerequisites: "armor innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a foe [[Grabbed]].

Your armor includes flame-resistant gauntlets with oil-filled finger joints. These joints can split apart, dousing your opponent in flammable oil and then igniting it. The opponent must attempt a [[Reflex]] save against your class DC.
- **Critical Success** The grab ends.
- **Success** The grab ends, and the target takes 1 persistent,fire damage.
- **Failure** The target takes @Damage[(floor(@actor.level/2))[persistent,fire]] damage equal to half your level.
- **Critical Failure** The target takes @Damage[(@actor.level)[persistent,fire]] damage equal to your level.

**Source:** `= this.source` (`= this.source-type`)
