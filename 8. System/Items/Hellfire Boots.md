---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Fire]]", "[[Invested]]", "[[Occult]]"]
price: "{'gp': 3000}"
usage: "wornshoes"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These heavy boots are made of blackened metal and always feel warm to the touch, with streams of glowing embers cascading off their heels. While wearing *hellfire boots*, you gain resistance 10 to fire damage.

**Activate—Devil's Dance** `pf2:2` (manipulate)

**Frequency** once per minute

**Effect** You Stride. Each square you move through during your Stride is scorched with hellish flames, becoming hazardous terrain for 1 minute. A creature that moves through one of these spaces takes 3d6 fire damage.

**Source:** `= this.source` (`= this.source-type`)
