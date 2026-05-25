---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Primal]]"]
price: "{'gp': 325}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Animal claws are woven into the thick leather of these bracers.

**Activate—Extend Claws** `pf2:1` (manipulate, morph)

**Frequency** once per hour

**Effect** The bracers fuse temporarily with your forearms, with the claws extending to your fingertips. You gain a climb Speed of 20 feet and a claw unarmed attack with the agile and finesse traits that deals 1d6 slashing damage. This lasts for 10 minutes or until you Dismiss it.

> [!danger] Effect: Clawed Bracers

**Source:** `= this.source` (`= this.source-type`)
