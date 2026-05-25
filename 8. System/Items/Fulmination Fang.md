---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Combination]]", "[[Concussive]]", "[[Kickback]]", "[[Magical]]"]
price: "{'gp': 115}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The stock and barrel of this *+1 striking gun sword* are lined with scales from a storm snake. Their insulating properties grant their wielder some protection against electricity.

**Activate—Lightning Rod** R

**Trigger** You take electricity damage

**Effect** You gain resistance 5 to the triggering damage, and the *fulmination fang* crackles with the absorbed energy. You can Interact to change between the gun sword's current usage (melee to ranged, or ranged to melee). The next melee Strike you make with the *fulmination fang* within the next minute deals an additional 1d6 electricity damage. After a minute, the absorbed energy dissipates.

> [!danger] Effect: Lightning Rod

**Craft Requirements** The initial raw materials must include the scales of a storm snake.

**Source:** `= this.source` (`= this.source-type`)
