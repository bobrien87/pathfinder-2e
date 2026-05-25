---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 55}"
usage: "affixed-to-firearm-with-a-reload-of-1"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a firearm with a reload of 1

**Activate** `pf2:f` (concentrate)

**Trigger** You miss on a ranged Strike with the affixed weapon using an ordinary 0-level piece of ammunition.

This small magnetite block is attached to the barrel of the firearm by a thin metal wire drilled through a hole in its center. When you activate the lodestone, the ammunition from your missed shot is immediately recalled to your firearm, allowing you to fire again without reloading.

**Source:** `= this.source` (`= this.source-type`)
