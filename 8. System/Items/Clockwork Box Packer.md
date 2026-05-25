---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Clockwork]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "4"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This handy clockwork device is too expensive for most warehouses and shipping docks to make use of it, but some nobles have purchased the item for their staff as a status symbol, and merchants who are in the shipping trade can afford to slowly reap the benefits of its usage. It takes 1 minute to wind a clockwork box packer; after which, it can function for up to 1 hour.

You can indicate how high you want the clockwork box packer to stack boxes and what the packing storage dimensions are. Once packing instructions have been input, you can load a crate onto the clockwork box packer, and it begins its task. Once the box is stacked, the clockwork box packer closes the box, if necessary, then ties a ribbon or cord around it from a supply loaded into the clockwork box packer in advance. Once the package is secure, the clockwork box packer stacks it and then swivels back into position, ready to accept another box. In this way, the clockwork device can finish within minutes a packing job that might take humanoid workers an hour

**Source:** `= this.source` (`= this.source-type`)
