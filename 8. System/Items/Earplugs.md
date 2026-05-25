---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "worn"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These small pieces of cloth and stuffing have been crafted to dramatically muffle sound and easily slide into and out of the ear canals of humanoid creatures. You can insert or remove earplugs from your ears or a willing creature's ears with a single Interact action using one hand. They take a -2 circumstance penalty to all auditory Perception checks but also gain a +2 circumstance bonus to saving throws against auditory effects.

**Source:** `= this.source` (`= this.source-type`)
