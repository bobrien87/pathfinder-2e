---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 250}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather armor* has several large pouches along the sides of the torso as well as the front and back sides of the legs. While wearing this armor, you can quickly inflate these large pouches with air, allowing you to float in water.

**Activate—Flotation** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You inflate large pouches that allow you to float. You gain a swim Speed equal to half your land Speed. You can swim only along the surface of the water while this is active. You can stow the flotation devices as a 1-minute exploration activity. If the pouches take any damage (AC 10, Hardness 0), they quickly deflate, ending the effect.

**Source:** `= this.source` (`= this.source-type`)
