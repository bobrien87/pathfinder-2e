---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

These coatings come in different colors, each with a different special effect. A bottle of colorful coating contains enough to slather over one 5-foot square within your reach or space and is made with a special dispenser that enables you to coat the surface using only one hand. It's possible to use the coating on any surface that can be painted (subject to the GM's discretion). Colorful coating dries instantly, and its effect in the square you coated lasts for 1 minute. After that time, the coating turns to fine, inert powder, returning the square to its original condition unless otherwise noted.

Indigo colorful coating contains agents that destroy weaker objects. When applied to a surface or object, the coating treats the object's Hardness as 2 lower and deals 1d4 acid to the object each round. The damage this coating deals remains after the coating becomes inert.

**Source:** `= this.source` (`= this.source-type`)
