---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Disarm]]", "[[Finesse]]", "[[Magical]]", "[[Trip]]"]
price: "{'gp': 240}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking spiked chain*, strung with bloodied military insignia and other grisly trophies harvested from slain soldiers, is commonly used by hobgoblin commandants to motivate their troops. On a critical hit, the *chain of command* deals an additional 1d6 mental damage.

**Activate—Mercy of the Commander** `pf2:1` (concentrate)

The chain of command gains the nonlethal trait for 1 minute.

**Activate—Will of the Commander** `pf2:1` (concentrate)

**Requirements** Your last action was a critical hit with the chain of command

**Effect** You cast [[Command]] on the target of your critical hit with a DC of 22. Regardless of the outcome, the target is then immune to this effect for 24 hours.

**Craft Requirements** Supply one casting of [[Command]].

**Source:** `= this.source` (`= this.source-type`)
