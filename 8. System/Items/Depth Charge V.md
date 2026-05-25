---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 660}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

Carved with stylized images of water or aquatic life, depth charges that are fired underwater or at a submerged target function with their normal range increments and can hit no matter their normal damage type. This ammunition explodes if it hits a target underwater, dealing @Damage[11d6[bludgeoning]|options:area-damage] damage in a @Template[burst|distance:20] DC 32 [[Fortitude]] save according to its type. This burst doesn't extend out of the water.

**Source:** `= this.source` (`= this.source-type`)
