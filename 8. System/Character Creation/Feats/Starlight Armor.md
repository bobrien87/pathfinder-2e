---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Oatia Skysage|Oatia Skysage]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Oatia Skysage Dedication"
frequency: "once per day"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You armor yourself in the light of distant suns, shielding yourself from harm. The armor grants you resistance 7 to piercing, bludgeoning, and slashing damage. The armor also sheds bright light for 20 feet (and dim light for the next 20 feet).

Whenever an adjacent creature attacks you, the attacker must attempt a [[Will]] save against your spell DC at the end of its action. On a failure, it becomes [[Dazzled]] until the end of its next turn. Regardless of the result of the save, the attacker is temporarily immune until the end of its next turn. The dazzling effect has the light and visual traits.

When you reach 17th level, the resistance increases to 10.

*Note: A duration for this ability was not provided by Paizo. The effect linked here is set to 1 minute.*

**Source:** `= this.source` (`= this.source-type`)
