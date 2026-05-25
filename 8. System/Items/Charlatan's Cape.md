---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 980}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This bright red-and-gold cape is often interlaced with glittery threads and serves as a distraction. While wearing the cape, you gain a +2 item bonus to Deception checks.

**Activate—Puff of Smoke** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You cast [[Translocate]]. The space you leave and the one you appear in are filled with puffs of smoke that make anyone within [[Concealed]] until they leave the smoke or the end of your next turn, at which point the smoke dissipates. Strong winds immediately disperse the smoke.

**Source:** `= this.source` (`= this.source-type`)
