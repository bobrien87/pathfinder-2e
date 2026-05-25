---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can create a permanent stone object, either sculpting stone pulled directly from your kinetic gate or manipulating earth and stone around you. It must fit within one 5-foot cube that's adjacent to you and on solid ground, and you can make the object large enough to occupy the square. If you create the object underneath you or another willing creature, you cause the target to rise on top of the object; you can't create it under an unwilling creature. This impulse has an unlimited duration, but if you use Igneogenesis again, the object returns to its original location or form. You can spend 1 hour to use Igneogenesis as an exploration activity; in this case, the object is permanent and non-magical.

The object can't include any intricate parts or moving pieces. You can attempt a Crafting skill check as part of using this impulse to add details to your creation, such as a symbol, short message, or pattern (with the DC determined by the GM).

**Level (+3)** You can add an additional 5-foot cube to the object. Each cube must be contiguous.

**Source:** `= this.source` (`= this.source-type`)
