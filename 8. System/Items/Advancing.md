---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 625}"
usage: "etched-onto-heavy-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune charges up as you defeat your foes, driving you forward across the battlefield with every victory.

**Activate**`pf2:f` (concentrate)

**Requirements** Your last action or activity reduced an enemy to 0 Hit Points

**Effect** You Stride up to 15 feet. This movement doesn't trigger reactions. You can Burrow, Climb, Fly, or Swim instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
