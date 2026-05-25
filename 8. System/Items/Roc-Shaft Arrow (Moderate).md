---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "other"
bulk: "—"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** arrow

**Activate** `pf2:1` Interact

Each of these arrows is made from an immense roc's flight feather, most of whose vanes have been trimmed to expose the arrow's shaft. When an activated roc-shaft arrow hits a target, the arrow briefly grows a pair of avian wings and attempts to carry off the target. The target must succeed at a DC 27 [[Fortitude]] save or be moved to a space you choose within 15 feet (20 feet on a critical failure). If this would move the target into a hazardous space, this effect gains the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
