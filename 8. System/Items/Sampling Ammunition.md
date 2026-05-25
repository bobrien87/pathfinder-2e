---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 22}"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** arrow, bolt

The head of this arrow or bolt is a pointed glass cylinder with a hollow core. Upon hitting a corporeal creature, sampling ammunition captures a small portion of the target's skin, blood, and flesh. The sample falls to the ground below wherever the creature was hit. This sample is sealed and magically preserved inside its chamber, although it deteriorates normally once the cylinder is opened. Sampling ammunition can't collect samples from creatures made entirely of metal, stone, or other hard substances.

**Source:** `= this.source` (`= this.source-type`)
