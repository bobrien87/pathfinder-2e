---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Linguistic]]", "[[Mental]]", "[[Mythic]]", "[[Visual]]"]
prerequisites: "Prophesied Monarch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You command that your foes bow down before you or face your wrath. All enemies within 40 feet who can see and hear you must attempt a Will saving throw against your class DC or spell DC, whichever is higher. Regardless of the result, a creature is then temporarily immune to Kneel Before the Rightful Heir for 24 hours.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 3d6 persistent,mental damage.
- **Failure** The creature takes 6d6 persistent,mental damage.
- **Critical Failure** The creature takes 6d6 persistent,mental damage and is [[Clumsy]] 2 for as long as it's taking that persistent damage.

The persistent mental damage can be ended only if the creature Drops Prone in a location that you can see and doesn't Stand until their next turn. An affected creature is aware of this restriction.

**Source:** `= this.source` (`= this.source-type`)
