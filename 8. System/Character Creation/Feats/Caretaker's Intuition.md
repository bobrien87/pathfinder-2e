---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Jotunborn]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your forebears had a deep understanding of the natural world around them, and you've learned some of their knowledge and techniques. You are trained in Nature. If you would automatically become trained in Nature (from your background or class, for example), you instead become trained in a skill of your choice.

Additionally, while outdoors, you can spend 10 minutes to read the sky and determine upcoming weather. You get a general impression of weather up to 8 hours in advance. You can use this to determine that clear skies or a rainstorm are ahead, but you can't determine specifics like wind speeds and direction, or that a tornado would be occurring later.

**Source:** `= this.source` (`= this.source-type`)
