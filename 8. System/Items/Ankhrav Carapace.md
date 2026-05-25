---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 350}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather armor* has interlocking panels and short bristles along the outer edges of the arms and legs. While wearing this armor, you gain resistance 2 to acid damage.

**Activate—Dig** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The bristles along your limbs enable you to tunnel through dirt and sand. For 1 minute, you gain a burrow Speed equal to half your land Speed.

> [!danger] Effect: Ankhrav Carapace

**Source:** `= this.source` (`= this.source-type`)
