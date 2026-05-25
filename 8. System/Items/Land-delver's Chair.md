---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "worn"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A supramarine chair is a wheeled, water-filled bath or tank, originally designed by merfolk, for assisting aquatic people's mobility on land. The heavier-duty land-delver's chair functions as a [[Traveler's Chair]].

You increase your Speed to 20 feet or your swim Speed, whichever is lower.

**Source:** `= this.source` (`= this.source-type`)
