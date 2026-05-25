---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'gp': 27}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Containing neither eggs nor cream, an egg cream fizz contains milk or nut milk, sparkling water, and flavored syrup, frothed and chilled. Upon drinking, you feel lighter and more buoyant, gaining a +5-foot item bonus to your Speed for 10 minutes. During this time, you also gain another effect determined by the drink's syrup, which is chosen when the drink is created.

- **Chocolate** You gain a +1 item bonus to Acrobatics checks to [[Balance]], Maneuver in Flight, and Squeeze.
- **Strawberry** You gain a +1 item bonus to Athletics checks to Climb, [[Leap]], and Swim.
- **Vanilla** You can Step into difficult terrain.

> [!danger] Effect: Egg Cream Fizz

**Source:** `= this.source` (`= this.source-type`)
