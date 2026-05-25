---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Poison]]", "[[Potion]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Beginner Box: Secrets of the Unlit Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This liquid contains blood from a juvenile horned dragon. For 1 hour after you drink the potion, you can breathe out a magical cloud of poison. Exhaling this dragon breath uses a single action. The cloud of poison deals @Damage[2d6[poison]|options:area-damage] damage in a @Template[cone|distance:15], and each creature in the area must attempt a DC 19 [[Fortitude]] save. After you use the dragon breath, you can't do so again for 1d4 rounds.

**Source:** `= this.source` (`= this.source-type`)
