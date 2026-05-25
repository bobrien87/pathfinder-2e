---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm that has the scatter trait.

You pack your weapon with additional shot and powder, creating a risky but devastating wave of destruction. Make a ranged Strike with the firearm. The firearm's range increment increases by 20 feet and the radius of its scatter increases by 20 feet. The Strike gains the following failure conditions.
- **Failure** The firearm misfires, but it doesn't cause the other critical failure effects listed below.
- **Critical Failure** The firearm misfires and also explodes. It becomes broken, and it deals its normal weapon damage to all creatures in a @Template[burst|distance:20] centered on the firearm, with a basic Reflex save against your class DC. This damage includes any from the weapon's fundamental and property runes.

**Source:** `= this.source` (`= this.source-type`)
