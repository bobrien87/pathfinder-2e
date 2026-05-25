---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Fortune]]", "[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 75}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You replace your eyes with ones similar to an insect's or a crustacean's, which allow you to better pinpoint movement. Once per day when you attempt a flat check to target a creature that's [[Concealed]] from you, you can roll twice and take the better result.

**Source:** `= this.source` (`= this.source-type`)
