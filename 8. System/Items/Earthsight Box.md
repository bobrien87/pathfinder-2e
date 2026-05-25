---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Scrying]]"]
price: "{'gp': 575}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fine wooden box is inlaid with Dwarven runes, with hinges and a clasp of forged iron. The box contains a few handfuls of fine sand.

**Activate—Replicate Earth** 1 minute (concentrate, manipulate)

**Frequency** once per day

**Effect** You hold the box closed and, while envisioning the terrain, turn the box clockwise three times. When you open the box, the sand reveals, in miniature, the stone terrain surrounding you, to a range of 60 feet. This shows details of paths, hills, embankments, boulders, and even artificial structures like walls and ditches, as long as they're made of stone and earth. If you're underground, it reveals tunnels and voids in the earth within 60 feet at your current depth. The sand maintains its shape until you close the box.

**Source:** `= this.source` (`= this.source-type`)
