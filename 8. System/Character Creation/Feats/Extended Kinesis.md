---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kineticist]]"]
prerequisites: "Base Kinesis"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've refined the control you can exert over your elements. Add the following options to Base Kinesis.

- **Proliferate** You cause an existing element to expand. This works like the generate option, except that you can either create an equal quantity of the element in the same square as its source or in an adjacent square, or cause the element to expand to fill its square (making a flame bigger or turning a twig into a small tree, for example). After you proliferate an element, it reacts to the environment naturally—water you proliferated into thin air would splash back down, for example. This affects only natural forms of the element, not durable, crafted goods.

- **Regulate** (air, fire, metal, or water only) You change the temperature of an existing element, making it colder or warmer. This can snuff out a flame or turn water to ice or steam. After this change, the element cools or warms naturally unless you Sustain the impulse. An item that gets cold or hot enough (as determined by the GM) can be used as an improvised weapon that deals 1 cold damage or 1 fire damage in addition to the damage the GM determines for the improvised weapon.

- **Sculpt** (earth, metal, or wood only) Reshape an existing element into a small object of a design you choose. It looks crude and artificial on close examination. The sculpted element can be shaped into a functional short tool (or a long tool if your Base Kinesis can affect 1 Bulk or greater). It's too fragile and artificial to be used as a weapon or have any monetary value.

**Source:** `= this.source` (`= this.source-type`)
