---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Magical]]"]
price: "{'gp': 35}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This buckler (Hardness 3, HP 6, BT 3) has the appearance of a common wooden shield.

**Activate—Deploy Encampment** 1 minute (manipulate, structure) You pull a strap near the shield's enarmes to create a makeshift shelter that unfolds over the next minute. The shield becomes a pup tent until you spend another minute collapsing it. Within the tent is a satchel that holds 1 Bulk of [[Rations]] and replenishes every week.

**Source:** `= this.source` (`= this.source-type`)
