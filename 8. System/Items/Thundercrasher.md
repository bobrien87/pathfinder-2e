---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Concussive]]", "[[Scatter 10]]"]
price: "{'gp': 155}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While looking straight down the barrel of this *+1 striking blunderbuss*, the spark gun's magical core is visible amid several reflectors. All damage dealt by a thundercrasher is sonic damage. On a critical hit, the target must succeed at a Fortitude save against your class DC or be [[Deafened]] for 1 minute.

**Activate** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You overload the *thundercrasher* to emit chaotic sonic frequencies that soften earth and stone. When you next fire the *thundercrasher* it also partially liquefies any natural earth or stone surfaces within range of its scatter trait, making the area difficult terrain.

**Source:** `= this.source` (`= this.source-type`)
