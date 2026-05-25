---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Backstabber]]", "[[Combination]]", "[[Fatal d10]]", "[[Goblin]]", "[[Scatter 5]]"]
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

An explosive dogslicer is a sneaky, explosive weapon that often brings perverse joy to the goblins who use them. At first glance, it appears to be a triple-bladed dogslicer with an oversized guard.

**Source:** `= this.source` (`= this.source-type`)
