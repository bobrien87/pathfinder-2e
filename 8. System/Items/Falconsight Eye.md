---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 200}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This prosthetic eye resembles that of a bird of prey. Along with the abilities of the [[Magical Prosthetic Eye]], it allows you to strike foes at greater range and with impressive accuracy.

**Activate** `pf2:1` (concentrate)

**Frequency** once per hour

**Effect** You become keenly aware of your foes, even those seemingly out of reach. For 1 minute, you can close your eyes as a free action to see through a ranged weapon you're wielding, which reduces the penalty for firing into your weapon's second range increment from –2 to 0. This effect doesn't negate the [[Blinded]] condition.

**Source:** `= this.source` (`= this.source-type`)
