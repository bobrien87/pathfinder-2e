---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 50}"
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

This creamy tea is made from warm soy milk steeped with whole, dried chrysanthemum flowers and honey and brewed from when the sun first touches the horizon to when it has fully set. Consuming this tea causes mild drowsiness, aids in sleep, and protects from harmful mental effects. You gain a +1 item bonus to all saving throws against mental effects for 1 hour.

> [!danger] Effect: Peace in Dreams Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The effects last for 8 hours, and as long as you're asleep, the item bonus increases to +2.

**Source:** `= this.source` (`= this.source-type`)
