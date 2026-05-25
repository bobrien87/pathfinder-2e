---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Consumable]]"]
price: "{'sp': 2}"
bulk: "—"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a lure is attached to a combat fishing pole, it can be used to make thrown weapon attacks with a range increment of 20 feet, though the lure must then be reeled back in with an Interact action before the weapon can be used at range again (see the tethered trait). The ranged trip, tethered, thrown, and versatile P traits of the combat fishing pole only apply to thrown attacks made with a lure.

**Source:** `= this.source` (`= this.source-type`)
