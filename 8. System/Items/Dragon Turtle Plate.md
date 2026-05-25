---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Aquadynamic]]"]
price: "{'gp': 700}"
bulk: "3"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This harness of *+1 resilient half plate* is made from the shell plates of a dragon turtle and has the aquadynamic trait. To those who can craft with them, the dense organic plates on the dragon turtle's body are as valuable as the creature's hoard of gold.

**Activate** `pf2:r` (manipulate)

**Trigger** A creature adjacent to you targets you with a melee attack

**Effect** You roll the hefty plates of the *dragon turtle armor* toward the attacker to gain a +1 circumstance bonus to AC against the triggering attack.

**Craft Requirements** The initial raw materials must include the shell of a dragon turtle.

**Source:** `= this.source` (`= this.source-type`)
