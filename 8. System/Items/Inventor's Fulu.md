---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 50}"
usage: "affixed-to-an-innovation"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You critically fail an action with the unstable trait.

Some inventors in Tian Xia put fried snacks near their innovations, a charm to make devices behave as intended. The practice rubbed off on other inventors, who replaced the food with a drawing on an *inventor's fulu*. When you Activate the fulu, your critical failure becomes a failure, and you can spend just 1 minute to return your innovation to full functionality. The fulu then burns up, and its effects end.

**Source:** `= this.source` (`= this.source-type`)
