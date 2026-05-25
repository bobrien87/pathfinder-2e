---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Invested]]", "[[Magical]]", "[[Mythic]]"]
price: "{'gp': 22000}"
usage: "worn"
bulk: "—"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you invest this silver ring, choose a skill; you gain an item bonus to that skill equal to your doomed value.

**Activate—Tempt Fate** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** Your [[Doomed]] value would decrease

**Requirements** You currently have fewer than 3 Mythic Points

**Effect** Your doomed value doesn't decrease. You gain 1 Mythic Point.

**Source:** `= this.source` (`= this.source-type`)
