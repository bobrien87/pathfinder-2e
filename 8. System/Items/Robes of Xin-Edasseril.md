---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Comfort]]", "[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 40000, 'pp': 0}"
bulk: "L"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These robes, the traditional raiment of the runelord of envy, function as *+3 greater resilient antimagic greater energy-resistant explorer's clothing*. The energy resistance granted by these robes can be selected from acid, cold, electricity, or fire when you perform your daily preparations—without these preparations, the robes default to cold resistance. The robe's pockets function as a [[Retrieval Belt (Major)]].

**Source:** `= this.source` (`= this.source-type`)
