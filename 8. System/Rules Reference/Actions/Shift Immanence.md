---
type: action
source-type: "Remaster"
traits: ["[[Divine]]", "[[Exemplar]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

You shift your power, filling one of your ikons with your divine spark. That ikon softly glows with radiant light, emits subtle chimes as it moves, or is otherwise obviously empowered in a way that matches your growing divinity, granting the ikon the divine trait and granting you that ikon's immanence effects for as long as your divine spark is empowering it. Your spark is indivisible, so it can empower only one ikon at a time. You can also Shift Immanence to return your spark to the depths of your soul, leaving none of your ikons empowered.

**Special** In addition to the above usage, you can also Shift Immanence as a free action triggered when you roll initiative.

**Source:** `= this.source` (`= this.source-type`)
