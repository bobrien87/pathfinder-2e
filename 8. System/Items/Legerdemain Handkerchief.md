---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Extradimensional]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This frilled, silvery-gray handkerchief is a stylish tool for personal hygiene by all appearances, but it can be used to covertly make very small items vanish.

**Activate** `pf2:1` (manipulate)

**Requirements** The handkerchief is entirely covering an item of negligible Bulk

**Effect** The handkerchief transports the item it covers into its extradimensional space. The handkerchief can hold only one item within its extradimensional space at a time, so any item taken is replaced by any item already within the space. You can also use this action to expel an item already within the extradimensional space without replacing it. This activation can't be used on an attended item unless the creature with that item allows it. Placing the handkerchief over an item typically takes an Interact action.

**Source:** `= this.source` (`= this.source-type`)
