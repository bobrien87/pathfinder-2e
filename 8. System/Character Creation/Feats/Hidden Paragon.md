---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Rogue]]"]
prerequisites: "legendary in Stealth"
frequency: "once per PT1H"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You successfully use Stealth to [[Hide]] and become [[Hidden]] from all of your current foes, or use Stealth to [[Sneak]] and become [[Undetected]] to all your current foes.

When you slip out of sight, you disappear. You become [[Invisible]] for 1 minute, even if you use a hostile action. Not even [[Revealing Light]], [[See the Unseen]], or similar effects can reveal you, though creatures can still use the [[Seek]] action to locate you as normal.

**Source:** `= this.source` (`= this.source-type`)
