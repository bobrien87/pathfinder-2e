---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Divine]]", "[[Talisman]]"]
price: "{'gp': 7}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate)

When you activate this alabaster pendant, attempt to [[Administer First Aid]] using Medicine with a +1 item bonus to the check. If you succeed, and you were trying to stabilize, the target regains 1 Hit Point, losing the dying condition and becoming conscious as normal. If you succeed, and you were trying to stop bleeding, the bleeding ends.

**Source:** `= this.source` (`= this.source-type`)
