---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 160}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Vengeful demon's tears* is an infamously noxious spirit mixed into a potent magical cocktail and traditionally packaged in a gourd adorned with an engraving of a terrifying demonic face. Drinking it feels akin to lighting your throat on fire and putting it out with an herbal tonic. When you activate this potion, you gain the [[Quickened]] condition for 3 rounds and can use the extra action each round to Strike, Stride, or to take the following action.

**Release the Demon** `pf2:1` (concentrate, healing) You focus on the sensation of life burning within your flesh and gain 2d8 temporary Hit Points for 1 round.

> [!danger] Effect: Vengeful Demon's Tears

**Source:** `= this.source` (`= this.source-type`)
