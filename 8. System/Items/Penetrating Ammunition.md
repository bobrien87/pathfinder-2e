---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 400}"
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

This ammunition has a slender shape and a viciously pointed tip. When you activate and shoot *penetrating ammunition*, the Strike takes the shape of a @Template[line|distance:60] originating from you.

Roll one attack roll and compare the result to the AC of each target in the line. The ammunition ignores up to 10 of a target's resistance, and it can penetrate walls up to 1 foot thick with Hardness 10 or less. Each target that takes damage from this ammunition also takes 1d6 bleed.

If your attack roll result is a natural 20, you improve your degree of success only against the first target in the line, but you can still score a critical hit on other targets if your result exceeds their AC by 10 or more.

If you have access to your bow's critical specialization effect, *penetrating ammunition* applies that effect only against a target in the last square of the line.

**Source:** `= this.source` (`= this.source-type`)
