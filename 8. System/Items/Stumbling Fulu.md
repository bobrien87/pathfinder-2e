---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 10}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 hour

The kitsune who first created a *stumbling fulu* advised the user to tuck the fulu under the target's belt for maximum effect. When the creature to which the fulu is affixed completes a Stride action, the creature must attempt a DC 17 [[Reflex]] save. On a failure, some element of the armor the fulu is affixed to comes undone, making the wearer [[Clumsy]] 1. On a critical failure, the target falls [[Prone]] and is [[Clumsy]] 2. The clumsy condition remains until the target takes a total of 1 Interact action, plus 1 additional Interact action per value of the clumsy condition above 1, to properly reclothe itself. Once the fulu activates, it burns up, its magic lasting only as long as the conditions it has imposed.

**Source:** `= this.source` (`= this.source-type`)
