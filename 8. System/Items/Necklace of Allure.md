---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornnecklace"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Several sapphires are set along the length of this brilliant silver necklace. The necklace features an intricately carved pendant in the shape of a wolf's head. You gain a +2 item bonus to Deception and Diplomacy checks. When you invest the necklace, you either increase your Charisma modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Win Them Over** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You cast a 4th-rank [[Charm]] spell with a DC 38 [[Will]] save.

**Source:** `= this.source` (`= this.source-type`)
