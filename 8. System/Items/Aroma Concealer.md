---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Oil]]"]
price: "{'gp': 3}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (Interact)

This oily mix of herbs and natural detergents can be applied to a creature to reduce and cover any ordinary odors they produce. The creature receives a +2 item bonus to Stealth checks to [[Hide]] or [[Sneak]] against creatures using primarily smell. This bonus also applies to the DC to [[Track]] the creature by scent. The listed amount is enough to cover one Medium or smaller creature and takes 1 minute to apply. The effect lasts for 1 hour after applying.

**Source:** `= this.source` (`= this.source-type`)
