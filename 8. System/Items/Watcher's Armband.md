---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Detection]]", "[[Invested]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 500, 'pp': 0, 'sp': 0}"
usage: "wornarmbands"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Soldiers who wear this burgundy armband serve as law enforcement within the ranks of a nation's military, seeking out those who would commit crimes while in uniform. While wearing the armband, you gain a +2 item bonus to your Perception DC against Deception checks to Lie to you. In addition, you can cast [[Ring of Truth]] once per day as an innate 3rd-rank occult spell.

**Activate—Find the Plant** `pf2:1` (concentrate, detection, manipulate)

**Frequency** once per day

**Effect** Sometimes people aren't in control of their minds. You activate your armband, which, for the next minute, suddenly glows red if anyone within 30 feet of you is under the effect of a magical mental effect that is controlling their mind or body (such as [[Dominate]]).

**Source:** `= this.source` (`= this.source-type`)
