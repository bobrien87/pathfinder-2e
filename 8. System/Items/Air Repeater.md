---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Agile]]", "[[Repeating]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A thin-barreled firearm that uses a container of pressurized air instead of black powder to propel small metal bullets from an attached cartridge, the air repeater has fallen out of common use in Arcadia due to its poor stopping power, though it's still used occasionally for casual hunting and sport shooting. The air repeater and its longer-ranged, two-handed variant are still valued by some for their ability to allow a shooter to fire multiple rounds without needing to stop to reload or crank to a new chamber. A typical air repeater magazine holds 6 pellets.

**Source:** `= this.source` (`= this.source-type`)
