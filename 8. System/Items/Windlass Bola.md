---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Clockwork]]", "[[Nonlethal]]", "[[Ranged trip]]", "[[Thrown]]"]
price: "{'gp': 200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Clockwork mechanisms tick away inside the weights of these *+1 striking returning bolas*, spooling out more cord in midair.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The cord of the bola snakes out as you throw it, allowing the weapon to wrap around a group of enemies. You use the bolas to attempt a ranged [[Trip]] against all creatures in a @Template[burst|distance:5] within the weapon's first range increment. Roll a separate Athletics check for each target. Each attempt counts toward your multiple attack penalty, but don't increase your penalty until you have made all the attempts.

**Source:** `= this.source` (`= this.source-type`)
