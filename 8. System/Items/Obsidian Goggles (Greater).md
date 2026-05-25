---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1250}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sleek, black lenses of these goggles somehow make everything seem more brightly lit. While wearing the goggles, you gain a +2 item bonus to Perception checks involving sight.

**Activate—Darkvision** `pf2:1` (manipulate)

**Frequency** any number of times per day

**Effect** Adjusting your goggles, you gain darkvision until you deactivate it as an Interact action or the item is no longer invested by you, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
