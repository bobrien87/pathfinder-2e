---
type: action
source-type: "Remaster"
cast: "Passive"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

(one minute)

**Frequency** once per 10 minutes

**Effect** You can remove investiture from an item you currently have invested, and this investiture does not count against your daily limit. You can invest a new item in this item's place.

**Source:** `= this.source` (`= this.source-type`)
