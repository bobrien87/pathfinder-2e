---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These seemingly ordinary rectangular eyeglasses feature clear lenses framed in copper. When invested and worn, they rest perfectly on the bridge of the nose and can only be removed by the wearer. You gain a +3 item bonus to Crafting checks and any skill check made to Identify Magic. When you invest the spectacles, you either increase your Intelligence modifier by 1 or increase it to +4, whichever would give you a higher value. You must select the skills and languages the first time you invest the item, and whenever you invest the same artificer spectacles, you get the same skills and languages you chose the first time.

**Activate** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You cast a 3rd-rank [[Mending]] spell on an item you touch.

**Source:** `= this.source` (`= this.source-type`)
