---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These cute and unassuming toy monkeys are often dressed in loud clothing and carry a percussion instrument. It's activated once a creature moves adjacent to the square it sits in, at which point it leaps on the creature, scurrying about on its agile hind legs while it pounds on its instrument, riding the creature and raising a racket. The creature being assaulted by the monkey must find a way to escape its agitator either via flinging the monkey off with the `act escape show-dc=all dc=18` action or by breaking the monkey. The monkey has AC 19, Hardness 2, HP 10 (BT 5) and object immunities.

**Source:** `= this.source` (`= this.source-type`)
