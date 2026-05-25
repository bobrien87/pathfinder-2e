---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Oracle]]", "[[Sorcerer]]", "[[Wizard]]"]
frequency: "once per turn"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per turn

**Requirements** Your most recent action was to cast a non-cantrip spell.

**Oracle** You siphon spell energy into one weapon you're wielding, or into one of your unarmed attacks, such as a fist. Until the end of your turn, the weapon or unarmed attack deals an extra 1d6 force damage and gains the divine trait if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead (or one type of your choice if the spell could deal multiple types of damage).

**Sorcerer** You siphon spell energy into one weapon you're wielding or into one of your unarmed attacks, such as a fist. Until the end of your turn, the weapon or unarmed attack deals an extra 1d6 force damage and gains the trait of your bloodline's magical tradition if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead (or one type of your choice if the spell could deal multiple types of damage).

**Wizard** You siphon spell energy into one weapon you're wielding, or into one of your unarmed attacks, such as a fist. Until the end of your turn, the weapon or unarmed attack deals an extra 1d6 force damage and gains the arcane trait if it didn't have it already. If the spell dealt a different type of damage, the Strike deals this type of damage instead (or one type of your choice if the spell could deal multiple types of damage).

**Source:** `= this.source` (`= this.source-type`)
