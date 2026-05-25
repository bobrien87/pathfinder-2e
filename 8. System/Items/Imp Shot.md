---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 24}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

This black-and-red ammunition contains an egg-shaped capsule. When an activated *imp shot* hits, the capsule cracks open and releases a manifestation that resembles a Tiny imp that can't act in any way or provide benefits outside those described here. If the Strike misses the target, the imp appears, makes a rude gesture at you, and vanishes in a puff of sulfuric smoke. On a hit, though, the imp harries the target for up to 1 minute, remaining in the target's space, slapping, nipping, hurling insults, and moving with the target as it moves. A creature harried by the imp is [[Off Guard]] and takes a –2 circumstance penalty to attack rolls and skill checks. At the start of your turn on each round while the imp is active, you must attempt a DC 11 flat check. On a failure, the imp makes a final vulgar gesture at the target and vanishes in a cloud of brimstone.

> [!danger] Effect: Imp Shot

**Source:** `= this.source` (`= this.source-type`)
