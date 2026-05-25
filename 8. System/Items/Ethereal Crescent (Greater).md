---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Whetstone]]"]
price: "{'gp': 320}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This crescent-shaped shard of iridescent metal is strangely translucent, fading to a blurry outline when examined for too long. A weapon under the effects of a *greater ethereal crescent* gains the effects of an [[Astral]] rune for 1 minute. This does not count against the weapon's normal maximum number of runes.

> [!danger] Effect: Ethereal Crescent

**Source:** `= this.source` (`= this.source-type`)
