---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Esoterica]]", "[[Fortune]]", "[[Occult]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You break a trinket, such as a lodestone or jade pendant, in two, creating a sympathetic link between the halves that bridges distance. During your daily preparations, you perform a short ceremony where you gift one of the two halves to a willing ally. On that ally, you can cast spells and use thaumaturge abilities targeting your paired ally as though you are adjacent to each other, and the ally can cast spells targeting you in the same way. These effects last as long as you and the ally have their half; if either half leaves either of your possessions for even a moment, or if you establish a link with a new ally during your next daily preparations, the link breaks.

**Source:** `= this.source` (`= this.source-type`)
