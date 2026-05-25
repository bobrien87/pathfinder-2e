---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Primal]]"]
price: "{'gp': 700}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These soft leather boots are embossed with simple woodland scenes. The boots grant a +2 item bonus to Acrobatics and allow you to ignore difficult terrain from plants and fungi.

You also gain a 10-foot climb Speed while climbing plants or fungi and don't need to use your hands to Climb them.

**Source:** `= this.source` (`= this.source-type`)
