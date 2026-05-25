---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "worn"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bracelet has three charms depicting a dagger, a shield, and a rose. While wearing this bracelet, you gain a +1 item bonus to Thievery checks. Whenever you roll a success to free someone from manacles, it counts as two successes (three on a critical success).

**Activate—No Chains** `pf2:r` (manipulate)

**Frequency** once per day

**Trigger** A creature attempts to [[Grapple]] you

**Requirements** You are aware of the creature and aren't [[Off Guard]]

**Effect** The bracelet yanks your body in one direction, attempting to throw off your attacker's grip. You gain a +1 circumstance bonus to your Fortitude DC against the triggering Grapple.

**Source:** `= this.source` (`= this.source-type`)
