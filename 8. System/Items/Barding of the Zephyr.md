---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Companion]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 900}"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This light barding is covered in stylized wind motifs. When you suit up your animal companion, the barding adjusts to fit your animal companion regardless of its shape.

When your companion falls, wind picks it up from below; it gains the effects of [[Gentle Landing]].

**Activate—Take Flight** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You trace a finger along the wind motifs on the barding, granting your companion wearing the barding a fly Speed of 30 feet for 10 minutes. Even if the companion doesn't have the mount special ability, it can still Fly while being ridden.

> [!danger] Effect: Barding of the Zephyr

**Source:** `= this.source` (`= this.source-type`)
