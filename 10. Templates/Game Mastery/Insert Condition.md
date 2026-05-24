---
type: condition
source-type: "{source-type}"
traits: "{traits}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
