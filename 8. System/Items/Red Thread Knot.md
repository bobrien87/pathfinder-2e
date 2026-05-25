---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small length of red thread is knotted six times, with a loop at each end so it can either be worn as a bracelet or anklet, or hung from a strap.

**Activate—Untie Fate** R (concentrate, fortune)

**Trigger** You critically fail a save

**Effect** The knot unties one of its six knots, altering your fate in the process. Treat your saving throw as if you failed the check rather than critically failed the check. Once the sixth knot unties, it becomes a non-magical red thread.

**Source:** `= this.source` (`= this.source-type`)
