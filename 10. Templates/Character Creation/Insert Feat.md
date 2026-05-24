---
type: feat
source-type: "{source-type}"
level: "{level}"
traits: "{traits}"
prerequisites: "{prerequisites}"
access: "{access}"
frequency: "{frequency}"
trigger: "{trigger}"
requirements: "{requirements}"
source: "{source}"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= choice(this.prerequisites != null, "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null, choice(this.prerequisites != null, "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null, choice(this.prerequisites != null or this.access != null, "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null, choice(this.prerequisites != null or this.access != null or this.frequency != null, "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null, choice(this.prerequisites != null or this.access != null or this.frequency != null or this.trigger != null, "<br>", "") + "**Requirements** " + this.requirements, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
