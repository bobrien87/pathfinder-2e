---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Cleric]]", "[[Exploration]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Carefully etching a sacred image into a physical object, you steel yourself for battle. You can spend 10 minutes emblazoning a symbol of your deity upon a weapon or shield. The symbol doesn't fade until 1 year has passed, but if you Emblazon an Armament, any symbol you previously emblazoned, and any symbol already emblazoned on that item instantly disappears.

The emblazoned item is a religious symbol of your deity in addition to its normal purpose, and it gains another benefit determined by the type of item. The benefit applies only to followers of the deity the symbol represents, but others can use the item normally.

- **Shield** The shield gains a +1 status bonus to its Hardness. (This causes it to reduce more damage with the Shield Block reaction.)

- **Weapon** The wielder gains a +1 status bonus to damage rolls with the weapon.

> [!danger] Effect: Emblazon Armament

**Source:** `= this.source` (`= this.source-type`)
