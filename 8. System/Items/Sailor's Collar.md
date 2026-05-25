---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Veteran sailors like to wear this jaunty blue collar, tied with a small bow in the front and tucked into the belt. It can even save your life if you fall overboard. When wearing the *sailor's collar*, you gain a +1 item bonus to Athletics checks.

**Activate—Gasp for Air** `pf2:r` (air, concentrate)

**Frequency** once per day

**Trigger** You fail a Swim check

**Effect** Your collar inflates, giving you something to breathe from. You can breathe underwater for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
