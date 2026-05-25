---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Ranged trip]]", "[[Tethered]]", "[[Thrown 20]]", "[[Versatile p]]"]
price: "{'sp': 4}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The combat fishing pole is a sturdy and flexible pole that can be used as a weapon in melee. When a lure is attached to a combat fishing pole, it can be used to make thrown weapon attacks with a range increment of 20 feet, though the lure must then be reeled back in with an Interact action before the weapon can be used at range again (see the tethered trait). The ranged trip, tethered, thrown, and versatile P traits of the combat fishing pole only apply to thrown attacks made with a lure; throwing the pole itself leaves you with no practical way to retrieve it other than moving to its location and picking it up. A combat fishing pole can be used alongside fishing tackle to fish, and it adds its item bonus from weapon potency runes (if any) as an item bonus on checks to fish when used in this manner.

**Source:** `= this.source` (`= this.source-type`)
