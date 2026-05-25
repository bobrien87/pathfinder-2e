---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The interior of this heavy, brass *+1 full plate* is lined with waterproof fabric, especially covering the seams between plates. When worn, it provides a sealed environment that protects you from drowning as well as allowing you to move more freely while underwater.

**Activate—Deep Dive** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The deep sea plate enables you to breathe underwater and gives you a swim Speed equal to half your land Speed while in depths of 500 feet or less for 1 hour.

> [!danger] Effect: Deep Sea Plate

**Source:** `= this.source` (`= this.source-type`)
