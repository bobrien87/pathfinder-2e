---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 360}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

A glistening, tar-like substance that's displeasing to the touch coats a black tendril shot. When the activated ammunition hits a target, it exudes tendrils that encase the target, which must attempt a DC 31 [[Fortitude]] save saving throw. The ammunition's effects last until the target Escapes.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Slowed]] 1 but gains a +2 circumstance bonus to [[Escape]] the ammunition's effect.
- **Failure** The target is slowed 1.
- **Critical Failure** The target is [[Slowed]] 2.

**Source:** `= this.source` (`= this.source-type`)
