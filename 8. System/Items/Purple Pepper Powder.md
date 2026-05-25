---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This nearly black purple powder is made from the extremely spicy Kuthite's kiss pepper and is a favorite among the Sklar-Quah. When you eat a meal flavored with this purple pepper powder, you gain resistance 10 to fire and resistance 5 to poison for 1 hour.

> [!danger] Effect: Purple Pepper Powder

**Source:** `= this.source` (`= this.source-type`)
