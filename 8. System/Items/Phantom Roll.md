---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 13}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

A phantom roll contains vegetables, greens, and fine, clear noodles, all wrapped in transparent, edible starch paper and alchemically treated and laced with a tangy sauce. Upon eating the roll, you gain a +1 item bonus to Stealth checks you attempt during the [[Avoid Notice]] exploration activity. You can also Avoid Notice at full Speed or combine it with Investigate or Scout while moving at half Speed. These effects expire 24 hours after you eat the roll or when you make your next daily preparations, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
