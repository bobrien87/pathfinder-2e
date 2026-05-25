---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Versatile s]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As black as coal, this blade grows more potent in darkness. While in bright light, it functions as a *+1 shortsword* and doesn't appear to radiate a magic aura to [[Detect Magic]] or similar spells unless the spells are 4th rank or higher.

In dim light or darkness, the *gloom blade* becomes a *+2 striking shortsword*. Whenever you use the *gloom blade* to attack a creature you're undetected by, you deal 1d6 additional precision damage.

To upgrade the *gloom blade's* fundamental runes, start with the base *+1 shortsword*, but if you improve it beyond a *+2 striking shortsword*, the runes apply in dim light or darkness as well.

**Source:** `= this.source` (`= this.source-type`)
