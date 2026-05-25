---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 180}"
usage: "affixed-to-a-magical-staff"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (manipulate)

**Requirements** You prepared the staff.

This cluster of unworked ruby is bound to the top of a staff by silver wire. When activated, it adds one temporary charge to the staff. Any spells cast from the staff before the end of the turn expend these charges first. Any unused temporary charges are lost at the end of your turn.

**Source:** `= this.source` (`= this.source-type`)
