---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 10}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** arrow, bolt

**Activate** A (manipulate)

The shaft of a *beacon shot* is studded with tiny flecks of glimmering gemstones. When an activated *beacon shot* hits a target, it embeds itself into that target and spews sparks for 1 minute. If the target is [[Invisible]], it becomes merely [[Hidden]] to creatures who would otherwise be unable to see it. The sparks also negate the [[Concealed]] condition if the target was otherwise concealed.

A creature can remove the arrow or bolt by using an Interact basic action and succeeding at a DC 20 [[Athletics]] check.

**Source:** `= this.source` (`= this.source-type`)
