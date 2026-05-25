---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Fungus]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 9}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large blue toadstool glimmers with soft, magical light similar to moonlight. The spots of white adorning the mushroom's cap glow ethereally, as if illuminated from the inside, shedding dim light in a 10-foot radius.

**Activate—Ward Area** 10 minutes (concentrate, light, manipulate)

**Effect** You plant the toadstool in the ground, allowing it to connect to all living fungi and plant matter within 120 feet of its planting. For 8 hours, any corporeal creature that touches the affected matter even accidentally begins to glow with bright magical light in a @Template[type:emanation|distance:10], which persists as long as they remain within 120 feet of the planted mushroom. A creature can move through an area containing affected fungi and plant matter without touching it by treating the area as difficult terrain and succeeding at a DC 18 [[Acrobatics]] check.

**Source:** `= this.source` (`= this.source-type`)
