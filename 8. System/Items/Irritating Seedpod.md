---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

When you crack open this soft, spongy seedpod, you can use it as a catalyst when casting a [[Mist]] spell. When you do, irritating pollen fills the area for the spell's duration. Creatures in the area must attempt a DC 21 [[Fortitude]] save saving throw to avoid sneezing uncontrollably. On a failed save, the creature becomes [[Slowed]] 1 for 1 round. A creature that succeeds at this saving throw becomes temporarily immune to the irritating seedpod's pollen for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
