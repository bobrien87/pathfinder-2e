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

Red colorful coating contains rubbery compounds, turning any surface it covers into a trampoline. A creature or object that falls onto a square coated with red colorful coating takes no falling damage and bounces half again as high as the original fall. If the creature fell straight down, then with several bounces, it comes safely to a stop. If it was moving horizontally, its bounce continues in the same direction, with a distance determined by the GM. If the coating is on a wall, a creature pushed or Shoved into the wall bounces back half again as far and avoids taking any damage from being pushed into the wall. On a ceiling, red colorful coating is useful only in unusual circumstances, such as in an area where gravity is reversed.

**Source:** `= this.source` (`= this.source-type`)
