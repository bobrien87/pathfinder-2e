---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 3}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A simple circular or rectangle pan with a mesh on the bottom. Often used for sifting through dirt or mud to find gold, sifting pans can be used to search for many materials, depending on the size of the holes in the mesh.

**Source:** `= this.source` (`= this.source-type`)
