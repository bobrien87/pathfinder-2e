---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This astrolabe is fashioned of magically attuned platinum plates and rings and is inset with carefully measured ruby gems. The astrolabe's back is engraved with helpful charts, a calendar, and a maker's mark.

An astrolabe of falling stars can be used as a [[Mariner's Astrolabe]]. In addition, it can produce the following magical effect.

**Activate—Starfall** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** With a flick of your finger, you set the astrolabe's rule spinning, causing the inset rubies to become a blur. Choose a point within 100 feet. The astrolabe of falling stars calls down a brief rain of meteorites in a @Template[type:burst|distance:10] centered on that point, dealing @Damage[1d8[bludgeoning],1d8[fire]|options:area-damage] damage to creatures in the area (DC 19 [[Reflex]] save).

**Activate—Calculate** 1 minute (manipulate)

Astrolabes can be used for navigation in unfamiliar or featureless locations. To use an astrolabe, the holder must be trained in Survival. By spending 1 minute to measure the height of the stars and planets, a holder who knows the time and date can determine the latitude, and a holder who knows their latitude can determine the date and time. An astrolabe also grants a +1 item bonus to checks to identify celestial bodies.

**Source:** `= this.source` (`= this.source-type`)
