---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
usage: "worn"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Those who are in tune with nature understand well the transience of life and the migration of souls. Just as the moon waxes and wanes, so too are the candles of life lit and extinguished. The ritual for creating this item requires an animal sacrifice in direct moonlight, the belief being that creatures sacrificed in this way are blessed to reincarnate into better lives. While you have this silver, crescent-shaped necklace invested, your unarmed melee Strikes are silver weapons with the properties of the [[Ghost Touch]] rune.

**Source:** `= this.source` (`= this.source-type`)
