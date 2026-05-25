---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Light]]", "[[Reincarnated]]", "[[Visual]]"]
frequency: "once per day"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You're below 20 Hit Points. Many people report seeing a bright light before their death. You're one of these people, and at rare intervals when hope seems dim, the light exudes outward from your soul. You shed bright light in a 30-foot radius (and dim light for another 30 feet beyond that) until the end of your next turn. Enemy creatures in the area that rely on sight must attempt a [[Fortitude]] save equal to your class DC or spell DC, whichever is higher.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round and dazzled for 1 minute.
- **Critical Failure** The creature is blinded for 2 rounds and dazzled for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
