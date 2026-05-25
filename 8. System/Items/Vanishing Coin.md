---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 160}"
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

**Trigger** You attempt a Stealth check for initiative, but you haven't rolled yet

**Requirements** You are trained in Stealth

This copper coin dangles from a leather strip strung through a hole drilled in the center. Until activated, the coin becomes invisible for a few seconds at random intervals every few minutes.

When you activate the coin, it casts a 2nd-rank [[Invisibility]] spell on you, lasting until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
