---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 15000}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Princess Eutropia commissioned Taldor's Imperial College of Heralds to preserve the paws that fell off the Mantle of the Grogrisant. A few weeks later, the college presented this pair of boots. You gain a +3 item bonus to Athletics checks and saves against forced movement. When you invest in the boots, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Grogrisant Leap** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The Grogrisant's legendary strength and reflexes empower your movement. You Leap, doubling the vertical and horizontal distance of your Leap action. If you land adjacent to a creature, you can Strike that creature once as part of this action.

**Source:** `= this.source` (`= this.source-type`)
