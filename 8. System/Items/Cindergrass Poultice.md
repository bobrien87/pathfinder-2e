---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 33}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thick, waxy gel erases the effects of flame. It restores 2d12 healing Hit Points to a creature when applied to their body. If the creature has taken fire damage within the last minute, it restores additional Hit Points equal to the amount of fire damage the creature took within the last minute (maximum +10). Finally, the creature becomes immune to the effects of severe heat for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
