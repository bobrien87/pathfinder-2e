---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Finesse]]", "[[Sweep]]"]
price: "{'gp': 950}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A specialized *+1 striking thundering probing cane* made from strengthened spruce wood, a *batsbreath cane* is distinctive for its brass tip. The tip covers a small hollow in the wood that houses quartz crystals infused with latent storm magic.

**Activate** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You strike the cane firmly against the ground, causing a pin within the brass tip to tap the crystals and emit a sonic pulse. The pulse reverberates in a 60-foot radius for the next minute, with the cane acting as an antenna to receive the echoes. For 1 minute, as long as you remain in the area and are holding the cane, you gain hearing as a precise sense.

> [!danger] Effect: Batsbreath Cane

**Source:** `= this.source` (`= this.source-type`)
