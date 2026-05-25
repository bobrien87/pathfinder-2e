---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Primal]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate—Wave Fan** (manipulate)

**Frequency** once per day

**Effect** You cast your choice of one spell contained in your *tengu feather fan*. You can instead cast a cantrip you've gained from a heritage or an ancestry feat; this doesn't use up one of the fan's daily activations. This activation takes the spell's normal number of actions.

The spell's DC is your class DC or spell DC, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
