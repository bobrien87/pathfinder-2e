---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 1500}"
usage: "affixed-to-a-metal-weapon"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (concentrate)

Although solid, this orb of metal swirls with bright silver and dark iron colors, as if made of liquid. When you activate the *alloy orb*, select cold iron or silver. The affixed weapon functions as the chosen material for 1 minute, suppressing its original material. This orb works on weapons of any level.

> [!danger] Effect: Alloy Orb (High Grade)

**Source:** `= this.source` (`= this.source-type`)
