---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 1900, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lantern is made of weathered tin and is cold and moist to the touch. The interior of the lantern, where a wick or candle would normally be placed, is filled with thick, black smoke, and there's no way to open the lantern.

**Activate—Consuming Darkness** `pf2:3` (concentrate, darkness, death, manipulate, spirit)

**Frequency** once per week

**Effect** Pure, impenetrable darkness flows out of the lantern like smoke and simply eats the light. A @Template[type:emanation|distance:60] centered on the lantern is plunged into darkness for 1 minute. This darkness functions as a 4th-rank [[Darkness]] spell. When the darkness is created, it deals @Damage[6d8[spirit]|options:area-damage] damage (DC 30 [[Fortitude]] save) to all creatures within the area. Any creature reduced to 0 Hit Points from this damage is destroyed entirely, leaving behind only a shadow that will slowly fade over the course of a year.

**Source:** `= this.source` (`= this.source-type`)
