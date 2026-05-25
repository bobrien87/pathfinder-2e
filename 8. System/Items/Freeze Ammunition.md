---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Splash]]"]
price: "{'gp': 28}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (manipulate)

Freeze ammunition carries chilling reagents that activate on contact with the target. A creature hit by activated freeze ammunition takes cold damage instead of the weapon's normal damage type, plus 2 cold splash damage. Hitting a 5-foot-square surface successfully with freeze ammunition deals 2 cold splash damage and covers the space in a layer of ice. Each creature standing on the icy surface must succeed at a DC 20 [[Reflex]] save or DC 20 [[Acrobatics]] check or else fall [[Prone]]. Creatures using an action to move onto the icy surface must attempt either a Reflex save or an Acrobatics check to [[Balance]]. Creatures that Step or [[Crawl]] don't need to attempt a check or save. The ice melts after 1 minute, although unusually hot or cold temperatures can change this duration at the GM's discretion. Dealing at least 1 point of fire damage to the ice removes it instantly

**Source:** `= this.source` (`= this.source-type`)
