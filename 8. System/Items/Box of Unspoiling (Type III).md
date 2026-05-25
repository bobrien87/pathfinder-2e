---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Extradimensional]]", "[[Magical]]"]
price: "{'gp': 1640}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This storage container decorated with images of wildlife and berries is popular among Shoanti quahs and other nomadic groups. The box functions like a *spacious pouch*, holding 100 Bulk, and is inscribed with magic to keep its contents cool to allow for travel with perishable items like meat and fruit. Items in the box are kept fresh for up to a year.

**Source:** `= this.source` (`= this.source-type`)
