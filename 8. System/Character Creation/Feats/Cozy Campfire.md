---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Campfire Chronicler|Campfire Chronicler]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Consecration]]", "[[Divine]]", "[[Exploration]]", "[[Fire]]"]
prerequisites: "Campfire Chronicler Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 1 hour building a campfire in a single unoccupied square and whispering the stories of those you've met on your journeys. The campfire sheds bright light in a 30-foot radius (and dim light for the next 30 feet). The campfire can't be put out or get larger through mundane means; it instead burns out after your next daily preparations or when you use this ability again.

The first time each round a creature within the campfire's bright light performs an action with the attack trait, they must then attempt a [[Will]] save against your class DC or spell DC (whichever is higher). This is a divine curse effect, and you are aware of any attempt, although other creatures in the area are not.

> [!danger] Effect: Cozy Campfire
- **Critical Success** The creature is aware of the effect and can choose to disrupt their action. If they don't disrupt it, the campfire goes out.
- **Success** The creature is aware of the effect and can choose to disrupt their action. If they don't disrupt it, they become temporarily immune to the campfire's effects for 24 hours.
- **Failure** The creature takes a –2 status penalty to the action's attack roll and to all other attack rolls until the beginning of their next turn.
- **Critical Failure** The action is disrupted, and the creature takes a –2 status penalty to attack rolls until the beginning of their next turn.

**Source:** `= this.source` (`= this.source-type`)
