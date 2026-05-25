---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Kept in an airtight spray bottle, revealing mist is an alchemical concoction that creates a sticky and clinging mist of chemicals in a @Template[cone|distance:30] when sprayed. It doesn't affect visibility but causes [[Invisible]] creatures in the area to be [[Concealed]] rather than undetected. Revealing mist is ineffective in water or in areas with other factors affecting the spread of the mist, as determined by the GM. It remains in the area for 1 minute or until any significant wind disperses it, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
