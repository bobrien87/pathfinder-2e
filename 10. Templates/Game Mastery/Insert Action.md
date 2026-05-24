---
type: action
source-type: "{source-type}"
traits: "{traits}"
cast: "{cast}"
trigger: "{trigger}"
requirements: "{requirements}"
prerequisites: "{prerequisites}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= "**Cost** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null, "<br>**Prerequisites** " + this.prerequisites, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
