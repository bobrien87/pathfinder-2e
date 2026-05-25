---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 140}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This armor can be disguised with a mere thought.

**Activate—Costume Change** `pf2:1` (concentrate)

**Effect** You change the shape and appearance of this armor to appear as ordinary or fine clothes of your imagining. The armor's statistics don't change. Only a creature that's benefiting from truesight or a similar effect can attempt to disbelieve this illusion, with a DC of 25.

**Source:** `= this.source` (`= this.source-type`)
