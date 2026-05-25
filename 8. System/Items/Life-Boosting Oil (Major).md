---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 1300}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you apply sticky, stinging life-boosting oil, you gain fast healing 15 that starts the first time you take damage while the oil lasts. Once the fast healing starts, the oil remains effective for 4 rounds. However, the oil lasts only 8 hours, whether it provides fast healing or not.

> [!danger] Effect: Life Boosting Oil

**Source:** `= this.source` (`= this.source-type`)
