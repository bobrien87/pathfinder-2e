---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Sonic]]"]
price: "{'gp': 2750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

An aetheric irritant is a chime that can emit a subsonic frequency that otherworldly beings find unpleasant. When you Activate an aetheric irritant, you sound the chime and place it on the ground in a square within your reach. The aetheric irritant affects an area in a @Template[type:emanation|distance:30]. Creatures with the fey, spirit, or undead traits must attempt a DC 36 [[Will]] save when they enter the affected area and at the beginning of every turn they are in the affected area. Those who fail the save treat the area as difficult terrain until the beginning of their next turn. A creature that critically succeeds at the save is immune to all aetheric irritants for 24 hours. An aetheric irritant continues to hum until it shakes itself to pieces after 10 minutes of being activated or it is moved, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
