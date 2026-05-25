---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 460}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *swarmeater's clasp* features carved reliefs of verminous, swarming creatures. When you wear the clasp, you gain resistance 10 to physical damage from swarm creatures.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Requirements** a swarm creature is within your reach

**Effect** You thrust your hand into the swarm, draw forth a squirming mass of vermin, and devour it. You recover @Damage[(3d10+8)[healing]] Hit Points and deal the same amount of bludgeoning damage to the swarm. The Hit Point recovery is a vitality healing effect.

**Source:** `= this.source` (`= this.source-type`)
