---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1700}"
usage: "worn"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Military leaders or heads of state award these special medals to commend exemplary performance by their top soldiers. They're typically worn on a special strip of fabric near the lapel, but soldiers from different countries sometimes wear them in other places. No matter how many magical medals you have, they collectively count as one invested item.

The profile of the unicorn on this silver medal has a horn that extends slightly beyond the circular border. This medal is awarded in recognition of true righteousness and exemplary service to a cause.

**Activate—Unicorn's Grace** `pf2:r` (concentrate, healing, vitality)

**Frequency** once per day

**Trigger** You would regain Hit Points from a magical effect

**Effect** You regain an additional @Damage[4d6[healing]|traits:concentrate,healing,vitality] Hit Points.

**Source:** `= this.source` (`= this.source-type`)
