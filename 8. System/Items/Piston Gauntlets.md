---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Clockwork]]", "[[Deadly d6]]", "[[Monk]]", "[[Reach]]", "[[Shove]]"]
price: "{'gp': 2800}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The striking surface of this *+2 greater striking flaming pantograph gauntlet* releases a puff of fire each time it reaches the end of its linkage.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You supercharge the gauntlet's attack. Make a melee Strike. This counts as two attacks when calculating your multiple attack penalty. If this Strike hits, you deal an extra two dice of weapon damage.

**Source:** `= this.source` (`= this.source-type`)
