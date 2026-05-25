---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "worn"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This incredibly spacious bandolier can hold up to 4 one-handed crossbows or firearms that take no more than 1 action to completely reload (typically meaning that weapons with the capacity or repeating traits won't fit in the bandolier's holsters). A gunner's bandolier can be etched with runes as though it were a ranged weapon. When you invest the gunner's bandolier, you can attune it to each of the 4 weapons holstered in it.

**Activate** `pf2:1` (concentrate)

**Effect** You empower one of the attuned weapons in the bandolier, granting it the runes etched onto the gunner's bandolier and removing the runes from any previously drawn weapon. Then, you Interact to draw the weapon.

**Activate** `pf2:3` (concentrate)

**Effect** All weapons that were attuned to the bandolier when you invested it, not including any weapons you're currently wielding, return to the bandolier, and one of the returned weapons is automatically reloaded.

**Source:** `= this.source` (`= this.source-type`)
