---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Focused]]", "[[Invested]]", "[[Plant]]", "[[Primal]]"]
price: "{'gp': 21000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The base of this cloak is a thick layer of moss, but it slowly picks up native plants from each area it spends time in. You gain a +3 item bonus to Nature checks. You also suffer no effects from extreme cold and severe heat.

**Activate—Druidic Secrets** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast an order spell. If you don't spend this Focus Point by the end of this turn, it is lost.

**Craft Requirements** You are a druid.

**Source:** `= this.source` (`= this.source-type`)
