---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The sleek, black lenses of these goggles somehow make everything seem more brightly lit. While wearing the goggles, you gain a +1 item bonus to Perception checks involving sight.

**Activate—Darkvision** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** Adjusting your goggles, you gain darkvision for 1 hour.

> [!danger] Effect: Obsidian Goggles

**Source:** `= this.source` (`= this.source-type`)
