---
type: condition
source-type: "{source-type}"
traits:
source: "{source}"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, ", "), "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
