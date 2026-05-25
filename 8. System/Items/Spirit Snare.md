---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Mechanical]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 90}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This complicated snare is affixed with various crystals and Stasian coils attached to strange electrical relays, working on the same principles as etheric spirit singers. When an incorporeal creature enters its square, the device lets loose an ectoplasmic web that lashes around the creature's spectral form. The creature must succeed a DC 26 [[Reflex]] save saving throw or become [[Immobilized]] for 1 round. On a critical failure, the creature becomes [[Immobilized]] for 1 minute. In either case, the incorporeal creature can attempt to `act escape show-dc=all dc=26`.

**Source:** `= this.source` (`= this.source-type`)
