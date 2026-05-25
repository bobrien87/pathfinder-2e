---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Mechanical]]", "[[Poison]]", "[[Snare]]", "[[Trap]]"]
price: "{'gp': 120}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cute and unassuming dragon toy activates once a creature moves into its square. It then unleashes a rapid burst of toxic gas in a @Template[emanation|distance:10]. Those within the emanation when the snare is activated must attempt a DC 25 [[Fortitude]] save saving throw or take @Damage[3d6[poison]|options:area-damage] damage.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Sickened]] 1.
- **Critical Failure** The creature takes double damage and is [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
