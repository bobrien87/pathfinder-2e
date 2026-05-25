---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]", "[[Void]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This thin, black liquid imparts a bone-deep chill while rapidly repairing an undead creature's physical or spiritual form. When you dash *oil of unlife* onto an undead creature, or a living creature with void healing, the oil absorbs quickly into its body, and the creature regains @Damage[(3d8+10)[healing]]{3d8+10 Hit Points}. You can pour *oil of unlife* on an incorporeal undead; in this case, the creature absorbs the oil into itself.

**Source:** `= this.source` (`= this.source-type`)
