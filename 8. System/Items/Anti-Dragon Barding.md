---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Companion]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 200}"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Consisting of long steel spikes projecting from light barding, anti-dragon barding helps to protect vulnerable mounts and livestock from massive aerial predators, including dragons, griffons, and rocs.

An animal companion wearing anti-dragon barding gains a +2 item bonus to its Fortitude DC and Reflex DC against attempts to `act grapple`, `act reposition`, `act shove`, or `act trip` it, and a creature that successfully Grapples the animal companion takes 1d4 piercing damage.

**Source:** `= this.source` (`= this.source-type`)
