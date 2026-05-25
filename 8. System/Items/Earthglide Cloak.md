---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Earth]]", "[[Invested]]", "[[Occult]]"]
price: "{'gp': 6500}"
usage: "worncloak"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This brown-and-gold robe covers you from head to toe. Its weighty fabric doesn't move with the wind, instead hanging still as if carved of stone.

**Activate—Glide through Earth** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You Burrow through dirt and stone up to your land Speed, leaving no tunnels or signs of your passing. If you end your movement inside solid stone, you are forcibly expelled into the nearest open area, taking 1d6 bludgeoning damage for every 5 feet between the end of your movement and the open area.

**Source:** `= this.source` (`= this.source-type`)
