---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Auditory]]", "[[Commander]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Mental]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You and your allies are currently outnumbered by enemies on the battlefield.

Even though the fight seems to be surging against you and your compatriots, you know that a key ally can always turn the tide. Choose a target you are currently observing. You assail it with a list of reasons why it should join you and why its defeat if it does not is surely inevitable. The target attempts a [[Will]] save against your class DC with the following results.
- **Critical Success** The target is uninterested in joining you and is temporarily immune to further uses of this ability for 24 hours.
- **Success** The target is [[Stunned]] 1 as it is forced to consider the merits of your offer.
- **Failure** The target swaps sides and joins you for the duration of the battle. It gains the [[Controlled]] condition, but it can attempt a [[Will]] save whenever it takes damage or whenever you direct it to take an action that goes against its nature. On a success, the effect ends and it rejoins its former allies.
- **Critical Failure** As a failure, but the target is so impressed by your leadership that it thanks you for the privilege of fighting alongside you; if it is still alive at the end of combat, it turns over any coins, wealth or other monetary possessions it has as tribute.

**Source:** `= this.source` (`= this.source-type`)
