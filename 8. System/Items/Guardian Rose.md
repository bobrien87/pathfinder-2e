---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Healing]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 20}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You would be reduced to 0 Hit Points but not immediately killed.

This rose-shaped crystal brooch is a translucent bloodred. These talismans have saved the lives of many a soldier on the field of battle. When you activate a *guardian rose*, you avoid being knocked out and regain @Damage[(2d8+5)[healing]] Hit Points. However, this puts a strain on your body and you are [[Enfeebled]] 1 until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
