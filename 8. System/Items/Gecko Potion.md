---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

A *gecko potion* is a sticky, tawny brown liquid with flecks of sand suspended in it. For 5 minutes after drinking this potion, your fingertips sprout thousands of microscopic, bristled hairs that cling to objects, granting you gain a +1 item bonus to [[Climb]] and [[Palm an Object]] checks and to your Reflex DC against [[Disarm]] attempts.

> [!danger] Effect: Gecko Potion

**Source:** `= this.source` (`= this.source-type`)
