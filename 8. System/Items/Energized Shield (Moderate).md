---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1300}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This minor reinforcing steel shield (Hardness 8, HP 64, BT 32) is lined with pale silver that glows when struck. Whenever you use the Shield Block reaction, this shield becomes energized for 1 round.

**Activate—Energized Blast** `pf2:1` (force, manipulate)

**Frequency** once per 10 minutes

**Requirements** The shield is energized

**Effect** You direct the stored energy into a short blast, targeting a creature within 15 feet. The target takes 3d10 force damage (DC 28 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
