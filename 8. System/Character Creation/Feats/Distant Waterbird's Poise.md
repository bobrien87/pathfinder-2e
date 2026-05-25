---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Arcane]]", "[[Magus]]"]
prerequisites: "aloof firmament hybrid study, Spellstrike"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You hit a target with a [[Spellstrike]].

You flow around your foe, using the magic of your attack to carry you away. You [[Leap]], [[High Jump]], or [[Long Jump]], and this movement doesn't trigger reactions from the creature you hit. If you High Jump or Long Jump, you don't have to perform the initial Stride (nor do you fall if you don't Stride 10 feet).

The lightness of your steps persists after the jump, granting you the ability to land on or walk on the surface of water or other liquids until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
