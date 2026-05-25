---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Steam]]"]
price: "{'gp': 425}"
usage: "other"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hefty winch is powered by a small steam engine and includes a 100-foot length of steel cable, which enables you to haul a heavier load than you could with a hand cranked winch or comealong. A steam winch allows you to slowly pull a heavy load (usually up to 50 Bulk) along a flat surface or up and down a vertical expanse.

Attaching a steam winch to a device takes three Interact actions, while starting the winch (and getting it warm enough to operate) takes 10 minutes. Once in operation, a steam winch requires regular maintenance to function. Every 20 minutes, the boiler must be refilled and heat levels maintained.

**Source:** `= this.source` (`= this.source-type`)
