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

**Activate** A (concentrate)

Leafy stalks protrude from the shaft of this rustic arrow. When an activated *vine arrow* hits a target, the arrow's shaft splits and grows, wrapping the target in vines.

The target takes a –10-foot circumstance penalty to its Speeds for `r 2d4` rounds, or until it [[Escapes]] against a DC of 19. On a critical hit, the target is also [[Immobilized]] until it Escapes.

**Source:** `= this.source` (`= this.source-type`)
