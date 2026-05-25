---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 50}"
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

Fine lines of djezet sparkle in conduit shot. When you Activate it, you name up to four creatures, in addition to you, that the ammunition's magic works for. When a conduit shot hits a target, which can be a square, it remains intact. It moves with a creature it struck, unless the GM determines otherwise, until that creature regains any Hit Points. If it doesn't stick to the target, the active ammunition instead falls into the target's space, remaining active.

If you or one of the four selected creatures include the ammunition in the area of a spell that is 3rd rank or lower; has an area of a burst, cone, or line; and does not have a duration, the djezet in the ammunition flares in striations of red light, increasing the area of that spell. Add 5 feet to the radius of a burst that has a radius of at least 10 feet or to the length of a cone or line normally 15 feet long or smaller. For a larger cone or line, add 10 feet to the length. These increases are based on the spell's original area, ignoring any increases due to other effects, such as the [[Widen Spell]] feat. Increasing a spell's area destroys the ammunition, which otherwise remains active for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
