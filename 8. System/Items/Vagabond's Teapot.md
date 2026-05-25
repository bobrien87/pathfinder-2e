---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These ceramic teapots are highly valued by travelers. While the teapot is filled with water, a creature can use a single action with the concentrate trait to instantly heat the water to boiling, at which point the kettle whistles and the water inside begins to cool at a normal rate. While the water remains heated, it is piping hot, and a creature splashed with it takes @Damage[1d4[fire]|traits:nonlethal]{1d4 nonlethal fire damage}. Instead of filling the teapot with water, you can pour an elixir of 4th level or lower into the pot and use the following activation.

**Activate—Share Brew** 10 minutes (concentrate)

**Frequency** once per day

**Effect** The teapot magically increases the volume of the inserted elixir to produce four uses of the same elixir. Once an elixir has been brewed in the teapot in this way, further attempts that day to brew another elixir spoil the inserted liquid. Any brewed elixir not consumed by the time it cools (typically 10 minutes) loses its alchemical properties.

**Source:** `= this.source` (`= this.source-type`)
