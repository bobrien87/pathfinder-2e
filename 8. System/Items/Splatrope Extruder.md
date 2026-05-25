---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This portable nozzle-and-trigger assembly based on spider spinnerets can extrude and weave alchemical adhesives into temporary constructions. As an Interact action, you can attach a Glue Bomb to the extruder.

**Activate** `pf2:1` (manipulate)

**Requirements** A glue bomb is installed in the extruder

**Effect** The extruder converts the glue bomb into a 30-foot rope, whip, or net, depending on the nozzle die you choose when activating the device. The created object lasts for 1 hour. The DC to [[Escape]] a created rope (if used to bind a creature) or net is equal to the consumed glue bomb's DC and Escaping destroys the created object.

**Source:** `= this.source` (`= this.source-type`)
