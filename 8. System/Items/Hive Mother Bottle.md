---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This bottle is packed with dirt, though the shrunken corpse of an ankhrav hive mother is buried within. When you open the bottle, the effigy of a Huge ankhrav hive mother emerges, burrows up to 20 feet, and then erupts from the ground spraying acid, creating a @Template[square|distance:15]{15-foot-by-15-foot} pit that's 10 feet deep. Creatures standing in this area take @Damage[6d6[acid],1d6[persistent,acid]]{6d6 acid damage and 1d6 persistent acid damage} (DC 24 [[Reflex]] save). A success or critical success means the creature also leaps to safety, landing in the nearest space adjacent to the pit. A failure or critical failure means the creature falls into the pit. Climbing out of the pit requires a successful DC 22 [[Athletics]] check.

**Craft Requirements** Supply the corpse of an ankhrav hive mother.

**Source:** `= this.source` (`= this.source-type`)
