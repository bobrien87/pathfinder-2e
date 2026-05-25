---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Tiny silver hooks decorate these fine silk gloves. They grant a +1 item bonus to Thievery and allow you to cast [[Telekinetic Hand]] as an innate occult spell.

**Source:** `= this.source` (`= this.source-type`)
