---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Deadly d10]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Stealthy hunters can use this +1 magic shortbow to attack from hiding. If you use this bow to Strike a target that can't see you and you get a critical hit, the target takes an extra 1d6 damage.

**Source:** `= this.source` (`= this.source-type`)
