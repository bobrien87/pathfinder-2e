---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 2750}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

These sets of rockets come in pairs and strap onto existing footwear (or a creature's feet). Inserting them and aligning them properly takes 1 minute. When you Activate the blast boots, you can [[High Jump]] or [[Long Jump]], without the need to Stride first. Higher-level versions increase the distance of your High Jump or Long Jump.

When you Activate the major blast boots to High Jump, you can increase the vertical distance of your High Jump by up to 80 feet. When you Activate them to Long Jump, you can increase the horizontal distance of your Long Jump by up to 120 feet. Additionally, for 1 minute, the major blast boots remain active, allowing you to clumsily fly through the air for the duration. You gain a 30-foot Fly speed for the duration, but any time you Fly, you are [[Clumsy]] 1 until the start of your next turn.

> [!danger] Effect: Blast Boots (Major)

**Source:** `= this.source` (`= this.source-type`)
