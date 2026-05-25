---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Weapon Improviser|Weapon Improviser]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Weapon Improviser Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you make a Strike with an improvised weapon you're wielding, you gain a +1 item bonus to the attack roll, and you can have the Strike deal two weapon damage dice instead of the improvised weapon's normal number. If the attack is a critical hit, the improvised weapon breaks after the normal effects of a critical hit occur. If the item has a Hardness greater than your level, or if it's an artifact, cursed item, or other item that's difficult to break or destroy, it doesn't break but the attack is a normal hit instead of a critical hit. You can choose not to get any of the effects of Improvised Pummel on a Strike if you don't want to risk breaking the item. At 12th level, the item bonus increases to +2, and at 16th level, the Strike deals three weapon damage dice instead of the improvised weapon's normal number.

If you're benefiting from [[Handwraps of Mighty Blows]], you use the handwraps' item bonus if it's higher and can choose to use its number of damage dice. Any property runes from the handwraps also apply if you use the handwraps' number of weapon damage dice, provided they could apply to the improvised weapon (as determined by the GM).

**Source:** `= this.source` (`= this.source-type`)
