---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A brass ear is a short, flared tube with one end narrow enough to comfortably fit against the ear canal. When using a brass ear to listen through a door, window, thin wall, or similar barrier, if the barrier would normally increase the DC of your Perception check to hear sounds on the other side, the DC increases by only half as much as normal. It's not suitable for improving your hearing in general, a role better served by a hearing aid.

**Source:** `= this.source` (`= this.source-type`)
