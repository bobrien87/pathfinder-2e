---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Plant]]", "[[Primal]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Woody vines and branches curl and twist around each other, growing small twigs, leaves, and flowers across the surface of this prosthetic arm or leg.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** A branch grows from your prosthesis, quickly flowering and then producing `r 1d4` ripe and flavorful fruits. A creature can pick and eat a fruit with an Interact action to regain @Damage[(2d6+5)[healing]] Hit Points. The fruits wither away after 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
