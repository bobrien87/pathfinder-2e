---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Cold]]", "[[Consumable]]", "[[Magical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

his snare hides a tiny humanoid figurine made of enchanted ice among leaves or just beneath a thin layer of dirt in the square. The first creature to enter the snare's square crushes the statuette, releasing an incorporeal figure of chilly mist that grabs at the triggering creature, dealing 8d8 cold damage. The creature must attempt a DC 26 [[Fortitude]] save.
- **Critical Success** The creature takes no damage.
- **Success** The creature takes half damage and is [[Clumsy]] 1 for 1 round as the icy figure clings to its legs.
- **Failure** The creature takes full damage and 1d6 persistent,cold damage from the icy figure's embrace. It is clumsy 1 for as long as it takes this persistent damage.
- **Critical Failure** The creature takes double damage and 2d6 persistent,cold damage from the icy figure's embrace. It is [[Clumsy]] 2 for as long as it takes this persistent damage.

**Source:** `= this.source` (`= this.source-type`)
