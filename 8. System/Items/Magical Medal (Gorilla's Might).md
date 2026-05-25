---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 25}"
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

This steel medal resembles the head and upper body of a gorilla. It's typically given in recognition of physical prowess, and it grants you a +1 item bonus to Athletics checks to [[Climb]], [[Force Open]], [[High Jump]], and [[Long Jump]].

**Activate—Gorilla's Second Leap** `pf2:r` (concentrate, fortune)

**Frequency** once per day

**Trigger** You would fail but not critically fail an Athletics check to High Jump or Long Jump

**Effect** The gorilla on the medal beats its chest, giving you another chance. You reroll the failed check.

**Source:** `= this.source` (`= this.source-type`)
