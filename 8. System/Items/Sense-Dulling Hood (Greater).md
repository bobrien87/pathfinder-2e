---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 350}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Sometimes, an enemy's dangerous special ability makes relatively standard sensory capabilities a liability. From an ofalth emitting its stench to a banshee wailing, plenty of creatures use their prey's senses against them. A sense-dulling hood is a wide, single-use mask designed to be pulled from an airtight package and slipped over the head. The mask grants you a +4 item bonus to saving throws against auditory, olfactory, and visual effects for 1 hour. Since it dulls your senses without depriving you of them, the mask also imposes a –1 penalty to rolls and checks using Perception for the same duration.

> [!danger] Effect: Sense Dulling Hood (Greater)

**Source:** `= this.source` (`= this.source-type`)
