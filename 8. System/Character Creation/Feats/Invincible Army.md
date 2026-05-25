---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Field Propagandist Dedication"
frequency: "once per round"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

You enumerate the many virtues and victories of your chosen allies, creating a story of their invincibility so convincing that it is as good as the truth. Choose an ally you can see and attempt a [[Deception]] check or [[Diplomacy]] check against the hard DC for the target's level. On a success, the target gains resistance 5 to either bludgeoning, piercing, or slashing damage, chosen when you use this ability; the type of damage resisted is usually tied to the story you tell about the character, such as giving them piercing resistance after telling a story about the time they rushed through a rain of arrows to take on an enemy encampment.

You can instead attempt your check against a very hard DC for the target's level to give them resistance to two damage types, adding acid, fire, cold, electricity, and sonic to the damage types you can grant resistance to.

> [!danger] Effect: Invincible Army

**Source:** `= this.source` (`= this.source-type`)
