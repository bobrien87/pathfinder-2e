---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "wornheadwear"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Most merfolk have no problem surfacing for a while, but constant existence in the air is exhausting and demoralizing. A clever artisan off the coast of Arcadia came up with this solution—a sturdy frame that goes on the shoulders and supports a bubble-like helmet filled with water. A mouthpiece lets the wearer speak to the outside world, and a plant-based filtration system keeps the water at the appropriate level of freshness or brackishness for the wearer. Over the years, these contraptions have spread to most of the world's oceans, though many merfolk don't use them—some find the devices just too heavy and would rather deal with the dryness. The helms are especially popular with abyssal merfolk, who tint the glass dark to protect from the too-bright surface.

**Source:** `= this.source` (`= this.source-type`)
