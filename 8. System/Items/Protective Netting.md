---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Fortune]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "wornheadwear"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Troops fighting in locales filled with insects wear enchanted gauzy nets over their heads, draped from wide flat hats, to protect against swarms of stinging or biting creatures. While wearing protective netting, if you would be exposed to disease or injury poison from an attack, attempt a DC 17 flat check. On a success, you are not exposed.

**Activate—Flutter Net** `pf2:r` (manipulate)

**Frequency** once per day

**Trigger** A swarm enters your space

**Effect** Your protective netting flutters rapidly, keeping the swarm away. You gain a +1 item bonus to saving throws against effects originating from swarms for 1 minute.

> [!danger] Effect: Flutter Net

**Source:** `= this.source` (`= this.source-type`)
