---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Champion]]", "[[Oracle]]"]
prerequisites: "trained in Occultism or Religion"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By right of ritual or sheer stubbornness, you have claimed rulership of the land. Claim a defined territory, such as a small section of forest or river, or a district of a larger city. Within its borders, you can cast [[Detect Magic]], [[Guidance]], and [[Sigil]] as innate divine cantrips, and you gain a +1 circumstance bonus to `act make-an-impression` on creatures that have the celestial, fiend, fey, monitor, or spirit traits.

**Special** You and your land are linked. Changes to one mirror themselves on the other—if you're depressed, gray rain and clammy mist might set in. These effects have no immediate mechanical impact, but they might give clues about problems afflicting the land.

**Source:** `= this.source` (`= this.source-type`)
