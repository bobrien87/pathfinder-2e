---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 58}"
usage: "worn"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A silver charm bracelet, a sluggish bracelet appears to be a [[Bracelet of Dashing]], granting you a +1 item bonus to Acrobatics checks. If the curse goes unrecognized, you think you can Activate it to gain a +10-foot status bonus to your Speed for 1 minute. Instead, its activation is as follows.

**Activate** `pf2:1` (concentrate)

**Effect** You take a –10-foot penalty to your Speed for 1 minute, and the bracelet fuses to you. Thereafter, it grants you no bonus to Acrobatics checks, and it imposes a –5-foot status penalty to your Speed.

**Source:** `= this.source` (`= this.source-type`)
