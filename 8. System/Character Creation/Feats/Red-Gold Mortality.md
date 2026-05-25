---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Exemplar]]", "[[Ikon]]", "[[Void]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a weapon ikon

By channeling your divinity into a creature along with a strike, you can disrupt their ability to recover. The imbued ikon gains the following ability.

**Immanence** When you successfully damage an enemy with the ikon, a marking appears around the wound, painted in the red of mortal blood and the gold of divine ichor. When the target would regain Hit Points, such as from a healing effect or an ability like fast healing or regeneration, it must attempt a [[Will]] save against your class DC to determine the effects, and then the marking fades. The marking otherwise fades after 1 minute.
- **Success** The creature regains the full number of Hit Points that would be healed.
- **Failure** The creature regains only half the number of Hit Points as the contradictory energies swirl within it.
- **Critical Failure** The creature doesn't regain any Hit Points.

**Source:** `= this.source` (`= this.source-type`)
