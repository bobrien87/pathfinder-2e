---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You became partially unstuck from time and have learned how to manipulate your place in the flow of time. When you roll initiative, you can choose one of three options: either do nothing and roll initiative normally, stabilize your timestream, or destabilize your timestream and send it into intense fluctuations.

- **Stabilize your Timestream** (fortune) You don't roll initiative, and instead your initiative is equal to 10 + the modifier you would have used for initiative.
- **Destabilize your Timestream** (fortune) You don't roll initiative, and instead attempt a DC 11 flat check. On a success, your initiative is equal to 19 + the modifier you would have used for initiative, and on a failure, your initiative is equal to 1 + that modifier.

Additionally, if your initiative roll result is tied with an opponent's initiative roll, you go first.

Your manipulation of time grants you access to a number of abilities, some of which require a saving throw. The DC for these abilities is either your class DC or spell DC, whichever is higher, and is called your chronoskimmer DC

Chronoskimmer

**Source:** `= this.source` (`= this.source-type`)
