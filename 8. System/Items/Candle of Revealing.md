---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When lit, this black candle's eerie blue flame reveals the presence of [[Invisible]] creatures. Within a 10-foot radius of the lit candle, creatures don't benefit from the invisible condition. Their bodies are outlined, not fully visible, so they're [[Concealed]]. Once lit, the candle burns for 1 minute, after which the effect ends. If extinguished, it can't be relit.

**Source:** `= this.source` (`= this.source-type`)
