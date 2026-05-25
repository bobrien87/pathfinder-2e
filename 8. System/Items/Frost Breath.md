---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Cold]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 70}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bottle of frozen vapors is captured in the frozen peaks of the crown of the world. After inhaling frost breath, you gain resistance 5 to cold. You can exhale the frost breath as a single action to release a spray of frigid air in a @Template[cone|distance:15]. Each creature in the area takes @Damage[4d6[cold]|options:area-damage] damage with a DC 20 [[Reflex]] save. For 10 minutes, surfaces in the area are covered in ice, becoming difficult terrain and uneven ground (DC 20 [[Acrobatics]] check).

> [!danger] Effect: Frost Breath

**Source:** `= this.source` (`= this.source-type`)
