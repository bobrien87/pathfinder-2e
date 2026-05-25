---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Extradimensional]]", "[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 2500, 'pp': 0, 'sp': 0}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This belt is covered in small pouches that clasp with buttons of painstakingly carved stone. The belt is tied to an extradimensional space that can hold up to ten items of 1 Bulk or less. Anyone holding the belt can sense its contents, but only those who've invested it can store or retrieve items. Many retrieval belts are found with an item already inside.

**Activate—Store Item** `pf2:1` (manipulate)

**Requirements** There is room for an item in the belt

**Effect** One item you're holding with a Bulk of 1 or less vanishes into the belt's extradimensional space.

**Activate—Retrieve Item** `pf2:f` (manipulate)

**Requirements** An item is stored in the belt and you have a free hand

**Effect** The item stored in the belt appears in your hand. Neither Store Item nor Retrieve Item can be activated again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
