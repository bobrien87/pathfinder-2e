---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Marshal Dedication, trained in Diplomacy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become a brilliant example of dedication and poise in battle, encouraging your allies to follow suit. When you spend this action, attempt a [[Diplomacy]] check. The DC is usually an easy DC of your level, but the GM can assign a different DC based on the circumstances. The effect depends on the result of your check.

> [!danger] Effect: Stance: Inspiring Marshal Stance
- **Success** Your marshal's aura grants you and allies a +1 status bonus to attack rolls and saves against mental effects.
- **Failure** You fail to enter the stance.
- **Critical Failure** You fail to enter the stance and can't take this action again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
