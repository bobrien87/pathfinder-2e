---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Invested]]", "[[Magical]]", "[[Morph]]"]
price: "{'gp': 20}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These black leather goggle frames have no lenses. Instead, when a character puts them on and invests them, the wearer's eyes transform and lengthen into snail-like eyestalks. The wobbly eyestalks stretch out through the lens holes and up over the wearer's head on lengthened optic nerves.

**Activate—Looksee** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** By focusing hard, you can watch for enemies in all directions. You gain all-around vision for 1 minute; during this time, you can't be flanked.

> [!danger] Effect: Stalk Goggles

**Source:** `= this.source` (`= this.source-type`)
