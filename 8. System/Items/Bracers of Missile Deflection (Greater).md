---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These bracers are made from plates of durable dawnsilver and gleam like the summer sun.

**Activate** R (manipulate)

**Frequency** once every 10 minutes

**Trigger** A ranged weapon attack hits you but doesn't critically hit

**Requirements** You are aware of the attack and not off-guard

**Effect** The bracers send the missile off-course. You gain a +2 circumstance bonus to AC against the triggering attack. If this would cause the attack to be a failure, the attack misses you.

> [!danger] Effect: Bracers of Missile Deflection

**Source:** `= this.source` (`= this.source-type`)
