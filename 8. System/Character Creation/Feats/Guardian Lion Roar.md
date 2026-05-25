---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Inventor]]", "[[Sonic]]"]
prerequisites: "armor, construct, or weapon innovation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your innovation is augmented with plates shaped to resemble the gaping maws of guardian lions, which you can energize to expel a stream of sonic energy reminiscent of a lion's powerful roar. All creatures in a @Template[type:line|distance:20] from your innovation take @Damage[(max(2,(floor(@actor.level/2)-2)))d8[sonic]|options:area-damage] damage with a [[Fortitude]] save against your class DC. Creatures that fail this save become [[Off Guard]] for 1 round. The damage from this effect increases by 1d8 at 10th level and every 2 levels thereafter.

**Unstable Function** You press concealed switches in the guardian lions' plates, extending their reach and power. Add the unstable trait to Guardian Lion Roar. The range of your roar increases to a @Template[type:line|distance:60]. Creatures that succeed (but not critically succeed) at their save also become off-guard for 1 round. On a critical failure when attempting the flat check for this unstable action, you take sonic damage equal to your level instead of fire damage.

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
