---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 85}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** arrow, bolt

**Activate** `pf2:1` (concentrate)

The tip of this arrow is carved into the shape of a lidless eye. When an activated scouting arrow strikes a surface within the second range increment of the weapon it was fired from, the wielder of that weapon can [[Seek]] as though they were at the point of impact of the arrow using their normal senses. After this glimpse, the ammunition crumbles to ash.

**Source:** `= this.source` (`= this.source-type`)
