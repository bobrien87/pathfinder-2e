---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Electricity]]", "[[Fire]]"]
price: "{'gp': 45}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This foot‐long length of conductive cable is capped on both ends by grounded handles containing Stasian coils. These coils can be turned on or off as a single action. While on, the coils electrify the cable, dealing @Damage[1d6[electricity],1d6[fire]] damage in a thin precise line to anything the cable touches, though the cable is too unwieldy to use as a weapon. Electrocables are typically used to "cut" a thin straight line through metal. They ignore 10 points of a metal object's hardness.

**Source:** `= this.source` (`= this.source-type`)
