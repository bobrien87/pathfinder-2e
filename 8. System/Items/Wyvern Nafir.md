---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 950, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple trumpet is carved from a single wyvern horn. A wyvern nafir grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Wyvern Scream** `pf2:2` (auditory, concentrate, manipulate, sonic)

**Frequency** once per day

**Effect** You blast a draconic scream from the nafir. All creatures in a @Template[type:cone|distance:30] take @Damage[5d10[sonic]|options:area-damage] damage (DC 27 [[Fortitude]] save). On a failed save, the target is pushed back 5 feet (or 10 feet on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
