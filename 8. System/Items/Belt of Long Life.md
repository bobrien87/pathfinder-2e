---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornbelt"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick leather belt is engraved with imagery of an ancient tree. You gain 15 temporary Hit Points the first time you invest the belt in a day. When you invest the belt, you either increase your Constitution modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Call Upon the Ancient Life** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You draw upon the lifegiving energy of the tree on the belt to gain rapid healing. For 2d4 rounds, at the start of your turn each round, you recover 15 Hit Points.

**Source:** `= this.source` (`= this.source-type`)
