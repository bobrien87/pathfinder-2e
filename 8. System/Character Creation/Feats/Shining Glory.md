---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "18"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your nimbus is active.

With a righteous word, your divine aura inspires your allies to great heroics and causes foes to tremble. Spend 1 Mythic Point. All allies in the bright light of your nimbus gain a +3 status bonus to attack rolls and skill checks, and the status bonus they receive to saving throws against fear increases to +3. These bonuses last for 1 minute or as long as they remain in the bright light of your nimbus, whichever comes first.

> [!danger] Effect: Shining Glory

Each enemy in the bright light of your nimbus attempts a [[Will]] save saving throw against your class DC or spell DC (whichever is higher) with the following effects. For the next minute, an enemy can't reduce its frightened condition below 1 while it remains in the bright light of your nimbus.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1, but can immediately Step as long it moves away from you.
- **Failure** The creature is [[Frightened]] 2 and you are [[Concealed]] to that creature while it has the frightened condition.
- **Critical Failure** The creature is [[Frightened]] 3 and you are [[Hidden]] to that creature while it has the frightened condition.

**Source:** `= this.source` (`= this.source-type`)
