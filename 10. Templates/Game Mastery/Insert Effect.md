---
type: effect
source-type: "{source-type}"
traits:
duration: "{duration}"
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`

`= choice(this.duration != null and this.duration != "", "**Duration** " + this.duration, "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
