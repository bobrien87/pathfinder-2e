---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Poison]]", "[[Splash]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A Strike

This flask is filled with a murky purple gas that briefly interferes with normal brain activity. A dread ampoule deals 3d6 mental damage and 3 mental splash damage.

On a hit, the target becomes [[Frightened]] 1, or [[Frightened]] 2 on a critical hit. Many types also grant an item bonus to attack rolls.

You gain a +2 item bonus to attack rolls.

**Source:** `= this.source` (`= this.source-type`)
