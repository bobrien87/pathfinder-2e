---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'gp': 65000}"
usage: "worn"
bulk: "—"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The fabric of this robe is infused with ever-shifting magical energy. The robe grants resistance 10 to acid, cold, electricity, and fire damage.

**Activate—Align Energy** `pf2:1` (concentrate)

**Effect** Spend 1 Mythic Point. You align the robe's magical energies to provide heightened protection against a specific damage type, at the expense of all the others. Choose acid, cold, electricity, or fire. The robe grants resistance 20 to the chosen damage type but no resistance to the remaining three types. The effect lasts until the next time you make your daily preparations (at which point the robe returns to normal) or until you use this activation again.

**Source:** `= this.source` (`= this.source-type`)
