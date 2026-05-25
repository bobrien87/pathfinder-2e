---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 250}"
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

*Mindlock shot* is made of luminous ectoplasm in a crystalline form. When you command this ammunition, you pick a Stride or Strike. If you hit a creature with the ammunition, it falls under a mental effect that makes it use its first action on its next turn to take the action you picked. It chooses exactly how to use that action, and if you choose Stride, the target can Step if doing so is beneficial for it. On a critical hit, the target must use its next 2 actions to do as you chose, within the same parameters.

**Source:** `= this.source` (`= this.source-type`)
