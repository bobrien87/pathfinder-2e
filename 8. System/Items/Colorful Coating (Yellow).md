---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 8}"
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

Yellow colorful coating contains a variety of compounds that fill small gaps and harden into a flat surface that increases friction, making it much easier to move on the square's surface. On the affected surface, the coating reduces difficult terrain caused by slipperiness, such as from ice or grease; this eliminates difficult terrain, reduces greater difficult terrain to difficult terrain, and reduces uneven ground to greater difficult terrain. The coating can't affect difficult terrain caused by features or effects not part of the surface, such as crowds, underbrush, wind, magic, and so on. The GM determines if yellow colorful coating can affect a surface's terrain.

The coating also makes a coated wall or ceiling easier to climb. It provides a +2 circumstance bonus to checks to Climb the coated surface.

Yellow colorful coating and green colorful coating have opposite effects. If they're both applied to the same surface, they negate one another.

**Source:** `= this.source` (`= this.source-type`)
