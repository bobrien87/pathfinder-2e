---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Force]]", "[[Magical]]", "[[Talisman]]"]
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

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt to [[Grab an Edge]] but haven't rolled

This pyramid-shaped spike is attached to an armor's chest piece. When you activate the spike, it shoots a strand of force to help you gain purchase, giving you a +1 item bonus to the check. If you roll a success on the triggering attempt, you get a critical success instead. If you roll a critical failure, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
