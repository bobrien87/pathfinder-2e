---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Planks of wood, embellished with carvings, spring forth to form a wall within 120 feet. The palisade is up to 30 feet long, 20 feet high, and 1 inch thick. It must form in a straight line in an unbroken open space that doesn't pass through any creatures or objects, or the impulse fails. When you create the wall, you can choose to create ledges on one side of the wall, 4 feet from the top, with ladders reaching to them from the bottom of the wall.

Each 10-foot-by-10-foot section of the wall has AC 10, Hardness 10, and 20 Hit Points, and is immune to critical hits and precision damage. The wall lasts until the end of your next turn, but you can Sustain it up to 1 minute.

**Level (+2)** The maximum length of the wall increases by 10 feet, and the HP of each section increase by 10.

**Source:** `= this.source` (`= this.source-type`)
