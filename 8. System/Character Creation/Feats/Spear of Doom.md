---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warrior Of Legend|Warrior Of Legend]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Warrior of Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** An enemy hit you with an attack dealing the same damage type as your cursed weakness within the last round, and you are [[Doomed]] 1 or greater.

The conditions for your doom have been met, and you brace yourself for a battle that will see you either live to fight another day or die a legend. You enter the spear of doom stance. While in this stance, as long as the enemy who triggered your cursed weakness is within your reach, you can Strike them as a reaction whenever they succeed or critically succeed at an attack against you. You gain an additional reaction immediately and at the start of each of your subsequent turns that can only be used to make Reactive Strikes against that opponent, or to make the Strike granted by this stance.

While in spear of doom stance, your cursed weakness is equal to your level instead of half your level.

**Source:** `= this.source` (`= this.source-type`)
