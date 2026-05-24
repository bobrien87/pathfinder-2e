---
type: effect
source-type: "{source-type}"
traits: "{traits}"
duration: "{duration}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= choice(this.duration != null, "**Duration** " + this.duration, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
