---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
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

This copper medal features a griffon's face, wings, and talons in profile. It is given in recognition of remarkable bravery, and it grants you a +1 item bonus to saving throws against fear and mental effects.

While wearing this pendant, you can also cast [[Forbidding Ward]] as an innate cantrip.

**Source:** `= this.source` (`= this.source-type`)
