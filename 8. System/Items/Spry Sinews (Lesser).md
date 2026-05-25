---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The tendons in your legs are uncommonly stretchy. When you [[Leap]], you increase the horizontal distance of your Leap by 5 feet and the vertical distance by 3 feet.

**Source:** `= this.source` (`= this.source-type`)
