---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Propulsive]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The kestros is a type of sling that fires special ammunition with wing-shaped fins and a pointed end. The thongs of the sling are of uneven length, one shorter and one several inches longer, around an open loop to cradle the ammunition as the sling is spun.

**Source:** `= this.source` (`= this.source-type`)
