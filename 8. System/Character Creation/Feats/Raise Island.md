---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]"]
prerequisites: "born of the bones of the earth or restless as the tide"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You churn the sea and fish up stone so your enemies together can receive their punishment. Each enemy in a @Template[type:emanation|distance:30] must succeed at a [[Fortitude]] save against your class DC or be swept up to 15 feet to another location of your choice within the affected area and become [[Off Guard]] until the start of your next turn. Then, if you're on a surface, a pillar of earth rises underneath you and lasts for 1 minute. The pillar is 10 feet tall, and its surface includes your space and a @Template[type:emanation|distance:5] around you. After the pillar rises, you can attempt a melee Strike against one enemy in reach.

**Source:** `= this.source` (`= this.source-type`)
