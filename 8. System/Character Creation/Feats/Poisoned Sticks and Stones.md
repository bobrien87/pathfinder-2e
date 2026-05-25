---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Guerrilla|Guerrilla]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Guerrilla Weaponry"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You prepare your sling stones with small, edged grooves to enable them to deliver poison, and you have learned other techniques for poisoning your weapons. You can apply injury poisons to sling bullets, allowing them to deliver such poisons on a successful Strike.

During your daily preparations, you can prepare a number of simple injury poisons equal to your level that can only be applied to sling bullets or blowgun darts. These follow the rules for injury poisons, except that they deal 1d4 poison damage with no saving throw. Only you can apply these poisons properly, and they expire at your next daily preparations.

**Special** If you later gain the [[Poison Weapon]] feat (such as from the poisoner archetype or the rogue multiclass archetype), you can apply your injury poisons to any weapon that is normally a valid receptacle for injury poisons, but you do not gain additional simple injury poisons during your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
