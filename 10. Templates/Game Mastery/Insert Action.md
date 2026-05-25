---
type: action
source-type: "{source-type}"
traits:
cast: "{cast}"
trigger: "{trigger}"
requirements: "{requirements}"
prerequisites: "{prerequisites}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
