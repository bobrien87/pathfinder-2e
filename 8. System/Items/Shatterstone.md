---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Sonic]]", "[[Splash]]"]
price: "{'gp': 380}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

A shatterstone is a small ceramic orb. Inside are reactive agents that set up an intense field of sonic vibration when the stone breaks. The bomb grants a +2 item bonus to attack rolls and deals 3d6 sonic damage and 3 sonic splash damage. Much of the sound is ultrasonic, and creatures with sonic weakness that take damage from the bomb must succeed at a DC 30 [[Fortitude]] save or be [[Deafened]] until the end of their next turn.

**Source:** `= this.source` (`= this.source-type`)
