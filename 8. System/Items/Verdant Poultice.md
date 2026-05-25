---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 27}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This poultice of herbs and dried berries found throughout Isger was invented by those fighting against Cheliax's diabolic intrusion and those warring against demons at the Worldwound. You can use a verdant poultice on a creature that's taking persistent damage from a fiend; attempt a [[Nature]] check with a +1 item bonus against the DC of the effect that caused the persistent damage. On a success, the persistent damage ends.

**Source:** `= this.source` (`= this.source-type`)
