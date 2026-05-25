---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Marshal Dedication, trained in Intimidation"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Putting on a grim face for the battle ahead, you encourage your allies to strike fear into their foes with vicious attacks. When you use this action, attempt an [[Intimidation]] check. The DC is usually an easy DC of your level, but the GM can assign a different DC based on the circumstances. The effect depends on the result of your check.

> [!danger] Effect: Stance: Dread Marshal Stance
- **Success** Your marshal's aura grants you and your allies in the aura a +1 status bonus to damage rolls. When you or an ally in the aura critically hit an enemy with a Strike, that enemy is [[Frightened]] 1. If you're wielding a weapon that has more than one damage die (typically due to a striking rune), you can have the status bonus equal the weapon's number of damage dice instead of +1.
- **Failure** You fail to enter the stance.
- **Critical Failure** You fail to enter the stance and can't take this action again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
