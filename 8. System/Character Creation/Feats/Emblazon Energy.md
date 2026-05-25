---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Cleric]]"]
prerequisites: "Emblazon Armament"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With elemental forces, you make your emblazoned symbols more potent. When you Emblazon an Armament, you can choose from the following effects instead of the effects listed in that feat. These effects have the same restrictions as the base options.

- **Shield** Choose acid, cold, electricity, fire, or sonic. The wielder gains the shield's circumstance bonus to saving throws against that damage type and can use Shield Block against damage of that type. The shield also gains resistance to that damage type equal to half your level if you have a domain spell with a trait matching that type (such as [[Fire Ray]]).

- **Weapon** Choose acid, cold, electricity, fire, or sonic. The weapon deals an extra 1d4 damage of that type. Increase this extra damage to 1d6 if you have a domain spell with a trait matching that type (such as *fire ray*).

> [!danger] Effect: Emblazon Energy

**Source:** `= this.source` (`= this.source-type`)
