---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Fortune]]", "[[Magical]]"]
price: "{'gp': 450}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This coin is struck with the image of a beatific seraph in gold on one side and a fearsome fiend with seven eyes enameled in black on the other. While it may seem nothing more than a curiosity, it's a powerful agent of fortune when activated.

**Activate** R (manipulate)

**Trigger** You fail a check or attack

**Effect** Flip the coin. If it lands on the seraph side, you get a 12 on the die instead of what you rolled. If it lands on the fiend side, one of the eyes on the fiend closes. Either way, you're temporarily immune to fortune's coin for 1 hour. When all seven eyes are closed, the coin vanishes into a puff of smoke, disappearing forever. This activation is a fortune effect, regardless of how the coin flip lands.

**Source:** `= this.source` (`= this.source-type`)
