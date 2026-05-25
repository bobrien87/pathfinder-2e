---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 24000}"
usage: "etched-onto-med-heavy-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *greater fortification* rune wards against the most deadly attacks. Each time you're critically hit while wearing the etched armor, attempt a DC 14 flat check. On a success, it becomes a normal hit. This property thickens the armor, increasing its Bulk by 1 and the Strength required to reduce its penalties by 1.

**Source:** `= this.source` (`= this.source-type`)
