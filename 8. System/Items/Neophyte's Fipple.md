---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 8}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` [[Perform]]

**Requirements** You are untrained in Performance.

Made of polished wood, a neophyte's fipple is a block flute enchanted to guarantee melodic sound. When you Perform a song on the fipple to Activate it, your attribute modifier, proficiency bonus, and item bonus for the Performance check total +7, regardless of what they would normally be. Add other bonuses and penalties to the check normally. Once the magic is used, the fipple remains as a mundane instrument.

**Source:** `= this.source` (`= this.source-type`)
