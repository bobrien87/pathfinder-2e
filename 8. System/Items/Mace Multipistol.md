---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Capacity 3]]", "[[Combination]]", "[[Concussive]]", "[[Fatal d8]]"]
price: "{'gp': 13}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

At first glance this weapon looks like nothing more than an iron-bound club. But the top of the weapon features a latch that opens to reveal three rotating pistol muzzles concealed in the mace's head that can be fired and rotated using triggers built into the weapon's haft.

**Source:** `= this.source` (`= this.source-type`)
