---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 1}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A trundle wheel is used to measure distance. It is a wheel attached to a handle so that it rolls along the ground. The wheel is often covered with leather or a rough metal to allow better grip on a surface and ensure it maintains traction. It's of an exact circumference, usually a yard or five feet. Each time it makes a complete rotation it makes an audible click so the user knows they have gone exactly that distance and can count the clicks to determine a longer distance traveled.

**Source:** `= this.source` (`= this.source-type`)
