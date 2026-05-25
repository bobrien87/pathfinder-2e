---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bull's-eye lantern is either stylized after an anglerfish or made from the taxidermy of one. While it can be lit as usual, the *anglerfish lantern* automatically shines when submerged in water.

**Activate—Mesmerizing Lights** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** All creatures within the bright light of the *anglerfish lantern* must succeed at a DC 19 [[Will]] save or be [[Fascinated]] by the light for 1 round (1 minute on a critical failure). The fascination ends if the light is extinguished. Aquatic animals and creatures with the water trait take a –2 circumstance penalty to this check. Regardless of the result, the creature then becomes immune to this effect for the next 24 hours.

**Source:** `= this.source` (`= this.source-type`)
