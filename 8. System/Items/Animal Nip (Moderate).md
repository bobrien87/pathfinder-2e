---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Olfactory]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Animal nip contains a mix of herbaceous, fragrant plants, ground into a coarse powder with a strong scent that attracts a broad spectrum of animals. You activate animal nip by sprinkling it on the ground or a target of your choice. For the next minute, all creatures within 30 feet that have the animal trait must attempt a DC 24 [[Will]] save or become [[Fascinated]] by the smell of the animal nip for 1 round. On a critical failure, they also fall [[Prone]] and roll about on the ground. If the target is subject to a hostile act, the fascination ends immediately. Regardless of the result of the creature's save, it's then immune to animal nip for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
