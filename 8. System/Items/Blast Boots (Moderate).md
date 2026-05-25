---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 11}"
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

These sets of rockets come in pairs and strap onto existing footwear (or a creature's feet). Inserting them and aligning them properly takes 1 minute. When you Activate the blast boots, you can [[High Jump]] or [[Long Jump]], without the need to Stride first.

When you Activate the moderate blast boots to High Jump, you can increase the vertical distance of your High Jump by up to 30 feet. When you Activate them to Long Jump, you can increase the horizontal distance of your Long Jump by up to 45 feet.

**Source:** `= this.source` (`= this.source-type`)
