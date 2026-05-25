---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 155}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

If fried, cast-off scales of a benthic worm render into crunchy snacks. Alchemists add reagents to the frying oil to enhance the scales' properties and flavor. For 1 minute after eating a delve scale, you gain a burrow Speed of 15 feet and a +2 item bonus to Athletics checks to [[High Jump]] or [[Long Jump]].

> [!danger] Effect: Delve Scale

**Source:** `= this.source` (`= this.source-type`)
