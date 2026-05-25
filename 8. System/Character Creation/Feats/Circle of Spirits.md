---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Apparition]]", "[[Concentrate]]"]
frequency: "once per round"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

With a thought, word, or gesture, you reach your mind out to another spirit. Choose another apparition from among those you've attuned to; it becomes your primary apparition, replacing your current one.

**Special** The number of Focus Points in your focus pool is equal to the number of focus spells you have or the number of apparitions you are attuned to, whichever is higher (maximum 3).

**Source:** `= this.source` (`= this.source-type`)
