---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Agile]]", "[[Deadly d6]]", "[[Magical]]", "[[Monk]]"]
price: "{'gp': 2100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking katar* masterfully crafted from the adamantine-laced fang of a shuln can puncture even the toughest of armors.

**Activate—Piercing Critical** `pf2:1` (concentrate)

**Frequency** once per round

**Requirements** Your last action was to score a critical hit with the *shuln fang katar* against a creature that is wearing armor

**Effect** You deal the same amount of damage as the critical hit to the creature's armor, bypassing any Hardness lower than 10, like adamantine.

**Craft Requirements** The initial raw materials must include a fang from a shuln.

**Source:** `= this.source` (`= this.source-type`)
