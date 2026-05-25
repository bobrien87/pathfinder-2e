---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As you strive to ascend to the ranks of celestials, the pull of gravity loosens on your body. You gain a fly Speed equal to your land Speed and the [[Flyby Attack]] action. When you gain this feat, you can choose to sprout wings, if desired; these wings are permanent.

Once per day as a single action, you can fly at incredible speeds. When you do, your fly Speed becomes equal to double your Speed for 5 rounds.

> [!danger] Effect: Ascend

**Source:** `= this.source` (`= this.source-type`)
