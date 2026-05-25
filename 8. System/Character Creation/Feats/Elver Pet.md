---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Athamaru]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Athamarus have bonded with eels more closely than any other fish. You have formed a strong connection with a young eel that serves as your pet. Typically, these eels are tended until they grow large enough to serve as a mount. You gain the [[Pet]] general feat. Instead of the normal choice of pet abilities, your eel has aquatic, [[Fast Movement]], and the [[Damage Avoidance]] familiar ability for Reflex saves. The aquatic ability means it gains the aquatic trait, breathes water instead of air, and has a swim Speed instead of a land Speed.

When you aren't in an aquatic environment, you can easily carry your pet eel around in a small water-filled globe that has light Bulk.

**Source:** `= this.source` (`= this.source-type`)
