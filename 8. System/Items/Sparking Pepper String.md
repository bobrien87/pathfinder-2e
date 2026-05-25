---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Electricity]]", "[[Processed]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Interact

Vendors sell these strings of roasted peppers on festival nights in Dhuraxilis. Their spiciness cuts through the fatty meats that are also popular during late nights, and the sparks from the peppers serve as a pick-me-up to maintain the energy for a party. After you eat a sparking pepper string, your body bristles with electricity until the end of your next turn. When you successfully Strike a target with an unarmed attack or a metal weapon, you can end this effect as a free action to have the attack deal an additional 1d6 electricity damage. If not expended before the duration ends, the electricity dissipates harmlessly.

> [!danger] Effect: Sparking Pepper String

**Source:** `= this.source` (`= this.source-type`)
