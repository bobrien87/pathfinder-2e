---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 325}"
usage: "wornbelt"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A feeling of security radiates out from this sash made of fine yellow fabric. You gain a +1 status bonus to saves against fear.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You and each ally in a @Template[emanation|distance:5] reduce your [[Frightened]] values by 1.

**Source:** `= this.source` (`= this.source-type`)
