---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 500}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 studded leather* armor was specially designed for removing locusts and similar vermin that had swarmed over portions of the battlefield. It's fully sealed along all of its seams with extra stitching and care, granting a +1 item bonus to Reflex saving throws against Swarming Bites, Swarming Stings, and similar abilities from swarms. In addition, you can create a cloud of smoke that can drive swarms from the area.

**Activate—Poison Fumes** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You emit a quickly fading toxic cloud around you in a @Template[type:emanation|distance:5]. All creatures within the emanation take @Damage[5d6[poison]|options:area-damage] damage (DC 24 [[Fortitude]] save). Swarms that fail this save also take 1d6 persistent,poison damage.

**Source:** `= this.source` (`= this.source-type`)
