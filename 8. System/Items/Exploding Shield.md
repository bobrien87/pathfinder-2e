---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 25}"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The magic within this wooden shield (Hardness 3, HP 12, BT 6) lashes out at your foes as the shield is destroyed.

**Activate—Splintering Boom** `pf2:f` (manipulate)

**Trigger** The exploding shield is destroyed

**Effect** The shield explodes outward, dealing 4d6 piercing damage to each creature in a @Template[cone|distance:15] (DC 19 [[Reflex]] save).

HardnessHPBT3126

**Source:** `= this.source` (`= this.source-type`)
