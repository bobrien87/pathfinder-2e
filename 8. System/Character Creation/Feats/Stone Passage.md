---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Divine]]", "[[Minotaur]]"]
prerequisites: "slabsoul minotaur heritage"
frequency: "once per PT1H"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Calling upon your knowledge of stonework and inherent magic, you momentarily make a section of stone insubstantial, allowing you to pass through. Stride up to your Speed. You can move through stone or rock objects, such as walls, as if they were unoccupied spaces. If you end your movement inside a square that you normally would not be able to pass through, you are thrown back to the last unoccupied square you moved into.

**Source:** `= this.source` (`= this.source-type`)
