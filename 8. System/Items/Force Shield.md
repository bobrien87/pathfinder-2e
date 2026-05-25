---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Force]]", "[[Magical]]"]
price: "{'gp': 650}"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The edges of this elaborately engraved steel shield (Hardness 8, HP 32, BT 16) bear tiny glass tiles set in mosaic patterns.

**Activate—Force Bubble** A (concentrate, force)

**Frequency** once per day

**Effect** The shield surrounds you with a bubble of force that protects you from harm, granting you resistance 5 to physical damage for 1 minute. The activation ends if you cease holding the shield.

> [!danger] Effect: Force Shield

**Source:** `= this.source` (`= this.source-type`)
