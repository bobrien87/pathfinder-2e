---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Fire]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 940}"
usage: "worn"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This black, metal ring is inset with rubies that occasionally give off wisps of smoke. It grants you a +2 item bonus to Athletics checks.

**Activate—Fire Jump** `pf2:2` (concentrate, manipulate, teleportation)

**Frequency** once per day

**Effect** You Stride (or Burrow or Fly, if you have the corresponding Speed) into any fire large enough to contain you, including magical fires. You vanish into the fire and take no damage from it. You can sense all sufficiently large fires within 100 feet of where you vanish, and you reemerge from any of those fires, either within the fire or adjacent to it. If you end your movement in the fire, it affects you as normal.

**Source:** `= this.source` (`= this.source-type`)
