---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 17}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

**Access** Tian Xia origin

White, pillowy dough surrounds an interior containing minced meats, spices, and herbs. The dough is steamed with elemental magic to make it light and airy while keeping the meaty center moist.

When you consume a bun, a set of small clouds form around your feet that grant you a fly Speed of 30 feet or your speed, whichever is lower, for 1 round.

> [!danger] Effect: Cloud Buns

**Source:** `= this.source` (`= this.source-type`)
