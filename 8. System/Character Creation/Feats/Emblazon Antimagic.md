---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Cleric]]"]
prerequisites: "Emblazon Armament"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your deity's symbol protects against offensive magic. When you Emblazon an Armament, you can choose from the following effects instead of the effects listed in that feat. These effects have the same restrictions as the base options.

- **Shield** When the wielder has the shield raised, they gain the shield's circumstance bonus to saving throws against magic, and they can use Shield Block against damage from their enemies' spells.

- **Weapon** When the weapon's wielder critically hits with the weapon, they can attempt to counteract a spell on their target, using half their level, rounded up, as the counteract rank. If they attempt to do so, the emblazoned symbol immediately disappears.

> [!danger] Effect: Emblazon Antimagic

**Source:** `= this.source` (`= this.source-type`)
