---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The red and dark-orange feathers of a pyrefowl have been woven into a beautiful cloak.

**Activate—Deflect Flame** `pf2:r` (manipulate)

**Trigger** You would be affected by a fire effect

**Frequency** once per day

**Effect** You flourish the cloak, using the feathers to reduce the incoming heat. You gain fire resistance 5 and a +1 circumstance bonus to saving throws against the triggering effect until the beginning of your next turn. If you are taking persistent fire damage, you can immediately attempt a flat check to end the persistent damage.

**Source:** `= this.source` (`= this.source-type`)
