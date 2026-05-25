---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Force]]"]
price: "{'gp': 600}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` Interact

Rusting ammunition is made using an ore louse's saliva and, when activated, deals damage to objects or creatures primarily made of metal. The target takes 4d8 persistent,force damage for up to 6 rounds. A creature that drops to 0 Hit Points while taking this persistent damage crumbles into fine powder; its gear remains. For an object, the ammunition destroys a 10-foot cube.

**Craft Requirements** Supply the saliva of an [[Ore Louse]]

**Source:** `= this.source` (`= this.source-type`)
