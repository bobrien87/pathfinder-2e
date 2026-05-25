---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 950}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can sense your surroundings using sonic pings rather than relying on your vision. You gain echolocation at 40 feet, allowing you to use hearing as a precise sense.

**Source:** `= this.source` (`= this.source-type`)
