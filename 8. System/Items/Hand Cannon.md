---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Modular]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Popular among privateers and mercenaries in Goka, hand cannons are little more than a hardened tube with a handle and external ignition attached. A hand cannon can be used to fire almost anything that can be packed into its barrel. The wielder of a hand cannon can change the damage type granted by its modular trait as part of the same Interact action used to reload.

**Source:** `= this.source` (`= this.source-type`)
