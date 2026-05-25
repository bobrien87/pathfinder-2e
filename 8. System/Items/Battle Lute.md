---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Shove]]", "[[Two hand d8]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This reinforced lute is suitable both for use as a handheld musical instrument and for bashing heads should a crowd turn sour. Its strings are finely braided wires that run along its sturdy metal neck. A battle lute adds its item bonus from weapon potency runes (if any) as an item bonus on Performance checks made while using it as an instrument.

**Source:** `= this.source` (`= this.source-type`)
