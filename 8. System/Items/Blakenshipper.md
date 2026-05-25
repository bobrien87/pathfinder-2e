---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 340}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This strange instrument is both played and worn, consisting of a set of pipes on a metal arm attached to a harness, a horn, a drum attached to a foot pedal, arm bellows, various keys, cymbals, and more esoteric elements. The blakenshipper grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Be the Band** `pf2:3` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You work double-time, playing an entire band's composition yourself, bolstering those around you by your mighty effort. You and all allies within a @Template[type:emanation|distance:60] gain 15 temporary Hit Points that last for 1 round. For the next minute, you can Sustain to continue the music, granting you and all allies within a @Template[type:emanation|distance:60] 5 temporary Hit Points that last for 1 round; this Sustain action gains the auditory and manipulate traits.

> [!danger] Effect: Be the Band

> [!danger] Effect: Be the Band (Sustain)

**Source:** `= this.source` (`= this.source-type`)
