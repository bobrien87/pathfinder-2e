---
type: item
source-type: "{source-type}"
level: {level}
traits: "{traits}"
price: "{price}"
usage: "{usage}"
bulk: "{bulk}"
activate: "{activate}"
source: "{source}"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null, "**Traits** " + this.traits, "")`

***

`= choice(this.price != null, "**Price** " + this.price, "") + choice(this.usage != null, choice(this.price != null, "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null, choice(this.price != null or this.usage != null, "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null, "**Activate** " + this.activate, "")`

***

{description}

**Source:** `= this.source` (`= this.source-type`)
