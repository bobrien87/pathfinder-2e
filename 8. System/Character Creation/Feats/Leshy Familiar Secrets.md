---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Druid]]"]
prerequisites: "leaf order"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The leaf order's secrets allow your familiar to take advantage of its leshy form. You can select one additional familiar ability each day, which must be one of the following leshy familiar abilities. You can't select more than one ability from this feat at a time.

- **[[Grasping Tendrils]]** Your familiar can extend vines or similar tendrils, increasing its reach to 15 feet.

- **[[Purify Air]]** Your familiar recycles air, providing enough oxygen for a Medium creature in areas with stale air, such as a sealed chamber or extradimensional space. Creatures within a @Template[emanation|distance:15] of the leshy gain a +2 circumstance bonus to their saving throws against inhaled poison effects, olfactory effects, or other effects that rely on breathing (such as toxic cloud), at the GM's discretion.

- **[[Verdant Burst]]** When your familiar dies, it releases its primal energy to cast the 3-action version of [[Heal]], heightened to a rank 1 lower than your highest-rank spell slot. The *heal* spell gains a status bonus equal to twice the spell's rank to the Hit Points it restores to plants. You must be able to cast 2nd-rank spells using spell slots to select this familiar ability.

**Source:** `= this.source` (`= this.source-type`)
