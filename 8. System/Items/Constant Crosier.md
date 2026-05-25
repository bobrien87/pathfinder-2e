---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weathered crook is often carried by chaplains of more primal deities. The carved wooden shaft bears the marks of fire damage and smells of campfire meals past. It counts as a wooden religious symbol for deities who grant the nature domain. While traveling in exploration mode, you and your allies within 120 feet count anyone's travel Speed of 15 feet or lower as 25 feet.

**Activate—Season of Grit** `pf2:1` (manipulate, visual)

**Frequency** once per day

**Effect** You brandish the constant crosier high in the air and wave it about. All allies within 60 feet who can see the crosier receive a +1 status bonus to Fortitude saves and resistance 5 to persistent damage for 1 minute.

> [!danger] Effect: Season of Grit

**Source:** `= this.source` (`= this.source-type`)
