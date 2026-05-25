---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 2200}"
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

Shiny gray metal that slightly thrums when touched makes up the metal parts of a magnetic shot. When activated, the shot is more effective against a target wearing metal armor or made of metal. The activated ammunition grants a +2 circumstance bonus to attack rolls against such targets. Due to magnetic acceleration, the ammunition deals four additional weapon damage dice and is deadly d12.

**Source:** `= this.source` (`= this.source-type`)
