---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Light]]"]
price: "{'gp': 3000}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+2 resilient fortification lattice armor* has latticework of fine golden wire. After negating a critical hit with its *fortification* rune, the latticework glows for 1 minute, shedding bright light in a 20-foot radius (and dim light for the next 20 feet). You can Dismiss this light.

> [!danger] Effect: Energizing Lattice

**Activate** `pf2:2` (concentrate, force)

**Requirements** The *energizing lattice* is glowing because it negated an enemy's critical hit

**Effect** You release the lattice's energy and make a weapon or unarmed attack Strike that deals 6d6 additional force damage. If your Strike fails, but doesn't critically fail, the target still takes half the force damage. The latticework ceases glowing after the Strike.

**Source:** `= this.source` (`= this.source-type`)
