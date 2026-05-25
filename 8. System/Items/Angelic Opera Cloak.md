---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This luxurious cloak embodies an angel's swiftness. You gain a +3 item bonus to Acrobatics checks and never take falling damage, as your cloak billows like a pair of wings to soften any fall you take. When you invest in the cloak, you either increase your Dexterity score by 2 or increase it to 18, whichever would give you a higher score. If you are unholy, you are [[Slowed]] 1 while wearing this cloak.

**Activate—On Angel's Wings** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** The opera cloak transforms into two pairs of brilliant, feathered wings that grant you a fly Speed of 40 feet for 10 minutes. During this time, you gain immunity to paralysis effects and ignore effects that would give you a circumstance penalty to speed.

**Source:** `= this.source` (`= this.source-type`)
