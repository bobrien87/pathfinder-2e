---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This masterfully crafted spirit is mixed into a potent magical cocktail and packaged in a gourd with an engraving of a dragon coiling around it. Drinking it imparts an intriguing balance of woodsmoke, honey, and bright floral top notes. When consumed, your arms become infused with the deadly power of a dragon's restless spirit. For 1 minute, your unarmed Strikes deal an additional 1d6 poison damage and an additional 1d6 void damage.

> [!danger] Effect: Ascendant Dragon Spirit

**Source:** `= this.source` (`= this.source-type`)
