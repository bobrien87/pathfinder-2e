---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt to Sense Direction

**Requirements** You're trained in Survival.

This fulu shows a series of constellations and arrows depicting astronomical movements through the night sky. When you activate a traveler's fulu, the magic infuses your mind with sensations of deja vu, as if you'd been in this region before. Your attempt to Sense Direction functions as if you have a compass, and you use the outcome one degree of success better than the result of your Survival check to Sense Direction, or by two degrees of success if you're a master in Survival.

**Source:** `= this.source` (`= this.source-type`)
