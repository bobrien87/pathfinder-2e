---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 1200}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You can spread this blue-gray gel on a single item with a Bulk of 3 or less to ward it against magical detection. It becomes immune to divination magic of 8th rank or lower (such as [[Locate]]). This oil is permanent, but it can be removed with acid. Removing the oil in this way usually takes 1 minute for objects with Bulk of 1 or less, or a number of minutes equal to the item's Bulk.

**Source:** `= this.source` (`= this.source-type`)
