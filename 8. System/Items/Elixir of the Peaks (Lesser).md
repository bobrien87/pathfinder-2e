---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]"]
price: "{'cp': 0, 'gp': 15, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

With much of New Thassilon located among the rugged heights of the Kodar Mountains, these elixirs have grown in popularity among those frequently travel the region. For 1 hour, drinking this elixir while in mountainous terrain protects you from the effects of severe cold and grants you a +1 item bonus to Athletics checks made to Climb, [[High Jump]], or [[Long Jump]], as well as to saving throws against the effects of high altitude.

**Source:** `= this.source` (`= this.source-type`)
