---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 60}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You take the [[Leap]] action.

Tradition says the dragonfly fulu should be affixed to the upper back, like the wings of an insect. When you Activate this fulu, you gain a +2 status bonus to Athletics checks to [[High Jump]] or [[Long Jump]] for 1 minute. During this time, you can attempt an Athletics check to High Jump or Long Jump as a single action without the Stride requirement. You can also High Jump or Long Jump from a nonsolid substance, such as air or water, but if you use this power of the fulu, its effects ends after you jump.

**Source:** `= this.source` (`= this.source-type`)
