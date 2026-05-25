---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 1800}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to armor

**Activate** A (concentrate)

This piece of bronzite is shaped like an oval with points at both ends. It has a carved flame at its center and is traditionally worn over the heart. You can activate only one *flame navette* per day. When you activate the navette, you gain the benefit of the fighter's [[Determination]] class feat, with a counteract rank of 8 and a counteract modifier of +22.

If you have the Determination feat, you can use your own modifier if it's better.

**Source:** `= this.source` (`= this.source-type`)
