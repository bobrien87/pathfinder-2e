---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Plant]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This tiny magic item looks like a ripe brown fruit from a kapok tree. Inside the fruit are three seeds. Each magical seed releases an effect when swallowed. The first grants you a +1 status bonus on Will saves against fear effects for 10 minutes. The second makes your next 10 words comprehensible to any creature that understands any language. The third lets you recall precisely how to get from where you are to any other place you've stayed for more than an hour within the past day. Once the seeds are removed, the fruit is edible, if chewed slowly, and quite tasty, being much sweeter than the non-magical version.

**Source:** `= this.source` (`= this.source-type`)
