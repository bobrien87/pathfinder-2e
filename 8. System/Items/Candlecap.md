---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 12}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The crown of a *candlecap* is stitched leather sewn in the shape of a small bowl. Fixed inside the bowl is a melted nub of wax with a small black wick.

**Activate** `pf2:1` (manipulate)

**Effect** You shake your head, and the candle wick ignites. The *candlecap* sheds dim light in a 20-foot radius. The candle doesn't require oxygen and can't be smothered or quenched. Activating the *candlecap* again douses the light.

**Source:** `= this.source` (`= this.source-type`)
