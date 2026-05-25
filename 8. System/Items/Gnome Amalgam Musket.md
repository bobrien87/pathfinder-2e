---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Combination]]", "[[Concussive]]", "[[Fatal d10]]", "[[Gnome]]"]
price: "{'gp': 10}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Rumored to be the result of a gnomish dare to make a variant of a hooked hammer that's even more intricate and complex, this weapon adds a musket to the mix of an already overcomplicated device.

**Source:** `= this.source` (`= this.source-type`)
