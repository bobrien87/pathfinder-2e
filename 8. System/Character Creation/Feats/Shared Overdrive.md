---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Inventor]]"]
prerequisites: "Overdrive Ally"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've experimented enough on your teammates to transfer a substantial number of powered-up gizmos to them, enabling one of your allies to benefit from the full effects and duration of your Overdrive. The first time you use Overdrive Ally during a given Overdrive, the effect lasts for the remainder of the duration of your Overdrive, instead of just until the end of the target's next turn. Any further uses of Overdrive Ally during the same Overdrive have their normal duration, per Overdrive Ally.

> [!danger] Effect: Overdrive Ally (Shared Overdrive)

**Source:** `= this.source` (`= this.source-type`)
