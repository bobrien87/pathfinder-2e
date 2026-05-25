---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 450}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather armor* has a metal exoskeleton that runs along your back and limbs and grants you increased strength for lifting and carrying. While wearing this armor, you can carry 2 more Bulk than normal before becoming encumbered and up to a maximum of 4 more Bulk.

**Activate—Heavy Lift** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** For 10 minutes, your physical strength is temporarily bolstered, granting you a +1 status bonus to Athletics checks to [[Disarm]], [[Reposition]], [[Shove]], and [[Trip]].

> [!danger] Effect: Lifting Leather

**Source:** `= this.source` (`= this.source-type`)
