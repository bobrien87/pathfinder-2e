---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Magical]]", "[[Wood]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A phrase of luck is carved into the handle of this wooden teaspoon. While a variety of other cutlery with similar properties exists, a spoon is often the most convenient and inconspicuous to carry.

**Activate - Purify** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You stir the spoon in food or drink, casting [[Cleanse Cuisine]] on the substance as you stir. This small spoon can purify up to 1 gallon of food or drink.

**Source:** `= this.source` (`= this.source-type`)
