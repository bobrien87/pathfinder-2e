---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 60}"
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

Though these preserved vegetables aren't actual moonflowers, they're made using a moonflower-distilled vinegar.

When consumed, tendrils sprout from your veins and curl around you, granting you a +2 status bonus to saves against void effects for 10 minutes and reducing your wounded condition by up to 2.

> [!danger] Effect: Preserved Moonflower

Eating more than one preserved moonflower dish in a day doesn't grant further benefits and makes you [[Drained]] 1.

**Source:** `= this.source` (`= this.source-type`)
