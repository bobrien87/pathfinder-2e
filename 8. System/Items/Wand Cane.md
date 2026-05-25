---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Though it appears to be a basic cane, the inner workings of the *wand cane* are an intricate network of lenses and magical circuits, with a slot at the top to insert a wand. The *wand cane* then spends 1 minute attuning to the wand, after which the wand can be used through the cane.

**Source:** `= this.source` (`= this.source-type`)
