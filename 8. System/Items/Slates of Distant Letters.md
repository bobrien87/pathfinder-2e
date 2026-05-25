---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2450}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This matched pair of slates, roughly one handspan wide and tall, have identical ornate frames. Slates are crafted in pairs, and each works with only the other of its pair. If one slate of a pair is ever broken, the other shatters into non-magical shards. The listed price is for a pair of slates.

**Activate—Send a Message** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You use a piece of chalk to write up to 25 words on a slate. As you write, the writing also appears on the other slate in its matched pair, no matter how far away it is, as long as it is on the same plane. Wiping one slate clean erases the writing from both slates. Each slate can be activated once per hour.

**Source:** `= this.source` (`= this.source-type`)
