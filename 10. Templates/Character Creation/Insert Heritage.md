---
type: heritage
source-type: "{source-type}"
ancestry: "{[[ancestry]]}"
traits:
prerequisites: "{prerequisites}"
source: "{source}"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

{description}

**Source:** `= this.source` (`= this.source-type`)
