---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 1850}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Magical writing covers the surface of this beautiful conch shell, which emits a blue light from inside. A *conch of otherworldly seas* is a virtuoso handheld musical instrument that grants a +2 item bonus to Performance checks attempted while using it.

The conch is a planar key for [[Interplanar Teleport]] and similar magic to travel to the Plane of Water. When using it this way, you can attune it to the waters of your destination to make it more likely to arrive where you intend to be, appearing 1d6×25 miles from your intended destination instead of 1d10×25 miles away.

**Activate—Voice of Oceans** `pf2:1` (manipulate)

**Effect** You hold the horn to your ear and can understand and speak Thalassic as long as it remains there.

> [!danger] Effect: Voice of Oceans

**Activate—Sounds of the Deep** 10 minutes (concentrate, manipulate)

**Effect** You hold the horn to your ear and touch the correct series of runes inscribed on its surface, causing the conch to cast a 5th-rank [[Clairaudience]] spell for your benefit. Provided you choose a location that's underwater, you can extend the spell's range to 1 mile and hear with perfect clarity.

**Source:** `= this.source` (`= this.source-type`)
