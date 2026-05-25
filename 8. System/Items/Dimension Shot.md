---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 360}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:2` (concentrate)

Dimension shot is deep blue black, but motes of light play upon it like stars in the night sky. The activated ammunition allows you to teleport to a location near where the ammunition hits. If you hit a creature, you can teleport to an unoccupied space adjacent to that creature. If you fire at a square, you can teleport to a space that contains that square or an unoccupied space adjacent to it. The teleportation fails if no unoccupied space is available to you

**Source:** `= this.source` (`= this.source-type`)
