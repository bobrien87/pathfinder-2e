---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 1300}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

An etheric essence disruptor emits bursts of discordant ethereal energy through a process based upon Stasian etheric-spirit singers, though without the need for a Stasian coil. Etheric essence disruptors attempt to break down the workings of a spell that manipulates spiritual essence. Upon activation, attempt to counteract an active divine or occult spell within 90 feet, with a +24 counteract modifier and a counteract rank of 8.

**Source:** `= this.source` (`= this.source-type`)
