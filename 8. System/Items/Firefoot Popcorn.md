---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you consume firefoot popcorn, for 1 minute, you can [[Leap]] double the normal distance. You can also attempt to [[High Jump]] or [[Long Jump]] as a single action. If you do, you don't perform the initial Stride (nor do you fall if you don't Stride 10 feet).

Each time you Leap 10 feet or more, your feet make a popping sound that can be heard from at least 100 feet, and the space you left fills with waves of intense heat. For 1 minute, that square is hazardous terrain that deals 1d6 fire to any creature that moves into it.

**Source:** `= this.source` (`= this.source-type`)
