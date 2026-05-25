---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 8000}"
usage: "affixed-to-armor-or-travelers-clothing"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Ablative armor plating is additional plating, combined with springs, clever clockwork, and improvised padding, to absorb damage by knocking the additional pieces free. The pieces slowly come apart on their own with time and movement. The process of attaching the plating takes 10 minutes and grants the wearer of the armor 40 temporary Hit Points for 1 hour or until lost. Removing the plating early destroys it.

> [!danger] Effect: Ablative Armor Plating (True)

**Source:** `= this.source` (`= this.source-type`)
