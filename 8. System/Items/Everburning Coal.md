---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Fire]]", "[[Magical]]"]
price: "{'gp': 1750}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lump of coal is always warm to the touch and glows faintly red from within, as if holding an ember of flame waiting to be stoked. No amount of water or coldness can extinguish the coal's warmth. When you hold an *everburning coal* in your hand, you gain resistance 10 to cold and are protected from mild, severe, and extreme cold.

In addition, an *everburning coal* is a planar key for [[Interplanar Teleport]] and similar magic to travel to the Plane of Fire. When using it this way, you can attune it to the fires of your destination to make it more likely to arrive where you intend to be, appearing 1d6×25 miles from your intended destination instead of 1d10×25 miles away.

**Activate—Coal Wall** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** The *everburning coal* creates a towering wall of hot coals. This has the effect of [[Wall of Ice]], except for the following adjustments.

- The wall has the fire trait instead of cold and water.

- The wall deals fire damage instead of cold damage.

- The weakness to fire is instead weakness to cold and to water.

- Destroying a section of the wall with cold or water (rather than with fire) causes a section to evaporate.

**Source:** `= this.source` (`= this.source-type`)
