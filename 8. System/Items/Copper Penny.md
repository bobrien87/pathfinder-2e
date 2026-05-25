---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 30}"
usage: "affixed-to-unarmored-defense-item"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You are knocked [[Prone]]

**Requirements** You're an expert in Acrobatics, and you are unarmored.

This plain copper coin is typically affixed near the feet, on a pant leg or hem. When you Activate it, you Stand and can't be knocked prone again on the current turn.

**Source:** `= this.source` (`= this.source-type`)
