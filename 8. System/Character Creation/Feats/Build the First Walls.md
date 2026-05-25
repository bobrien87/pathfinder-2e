---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Jotunborn]]", "[[Manipulate]]", "[[Occult]]"]
frequency: "once per day"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

The powers of creation that run through you allow you to conjure a temporary wall. You create a wall of dirt with the effects of [[Wall of Stone]] with the following exceptions. The wall can be up to 60 feet long and 10 feet high and must stand vertically, preventing you from building other structures with it. Each 10-foot-by-10-foot section of the wall has AC 10, Hardness 10, and 20 Hit Points. The wall remains for 1 hour or until Dismissed.

**Source:** `= this.source` (`= this.source-type`)
