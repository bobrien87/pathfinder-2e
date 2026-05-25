---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 230}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large bronze bell has a fine ash handle, and the clapper is made of blackened iron. It grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Clarion Crescendo** `pf2:2` (manipulate, sonic)

**Frequency** once per day

**Effect** You ring a blasting note on the bell that sends shock waves through the air. The blast deals @Damage[4d6[sonic]|options:area-damage] damage to each creature in a @Template[type:emanation|distance:15] (DC 22 [[Fortitude]] save). On a failure, the target is also [[Deafened]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
