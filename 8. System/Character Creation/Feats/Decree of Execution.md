---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "18"
traits: ["[[Death]]", "[[Incapacitation]]", "[[Mythic]]", "[[Spirit]]"]
prerequisites: "Prophesied Monarch Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You proclaim that a foe has violated the sanctity of your realm and must die. Speak your decree; a creature you designate within 60 feet who can hear your decree must attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher. Once targeted, the creature is temporarily immune for 1 year. Whether the target perishes or is marked for death depends on their level and the result of their saving throw.
- **Critical Success** The target is unaffected.
- **Success** If the target is 14th level or lower, it drops to 1 Hit point. If the target is 15th level or higher, it takes 50 spirit damage.
- **Failure** If the target is 14th level or lower, it dies instantly. If the target is 15th level or higher, it takes 50 spirit damage; if this damage brings it to 0 Hit Points, it dies instantly. Otherwise, it gains weakness 20 to all damage for 1 minute.
- **Critical Failure** As failure, but a target who survives the damage is [[Stunned]] 1 for 1 minute.

When you speak a Decree of Execution, you can spend a Mythic Point as part of the action to remove the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
