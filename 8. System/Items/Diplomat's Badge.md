---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 125}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When displayed prominently, this brass badge makes creatures find you more agreeable. You gain a +1 item bonus to Diplomacy checks.

**Activate—Diplomat's Bearing** A (concentrate)

**Frequency** once per day

**Effect** Attempt a DC 20 check to Recall Knowledge about people of a human ethnicity, a non-human ancestry, or some other type of creature. (The GM determines what your options are.) If you succeed, the badge's bonus increases to +2 for Diplomacy checks with creatures of that group for the rest of the day.

> [!danger] Effect: Diplomat's Badge

**Source:** `= this.source` (`= this.source-type`)
