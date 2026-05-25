---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 180}"
bulk: "3"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+1 splint mail* is worn by veteran sailors aboard warships who want as much protection as possible but still need to remain mobile enough to climb up rigging or swim should the need arise. The plates are arranged for maximum flexibility and the undercoat of padded armor is often no more than a cotton shrift. The armor grants you a +1 item bonus to Athletics checks to Climb or Swim and increases the distance you move when you successfully Climb or Swim by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
