---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 8}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You Stride or Step

**Requirements** You are trained in Acrobatics

This stone, usually shaped as a cabochon, is a small chunk of amber with a bit of feather or a flying insect caught within it. When you activate the stone, you ignore the effects of any difficult terrain and greater difficult terrain you move through until the end of your turn.

**Source:** `= this.source` (`= this.source-type`)
