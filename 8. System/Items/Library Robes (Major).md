---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Inscribed]]"]
price: "{'gp': 6000}"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These *+2 greater resilient scroll robes* magically store a spell for you. During your daily preparations, choose one spell you know of 8th rank or lower. You inscribe that spell on the robes, as though you had done so using the robes' inscribed trait, but without needing to go through the normal scribing process. You must provide the minimum amount of materials to Craft one scroll of that spell (typically half the Price of a scroll of that rank plus any extra cost required for the spell). You don't need to be trained in Crafting, nor do you need the [[Magical Crafting]] feat. Using this ability erases any scroll already inscribed on the robe.

**Source:** `= this.source` (`= this.source-type`)
