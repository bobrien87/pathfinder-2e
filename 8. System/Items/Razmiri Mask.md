---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This mask is made of iron, though more potent versions crafted by powerful Razmiran priests can be made of silver, gold, or even porcelain. The wearer of this mask gains a +1 item bonus to Deception checks to [[Lie]] or [[Feint]].

**Activate—Call Upon Razmir's Benevolence** `pf2:2` (concentrate, manipulate, occult)

**Frequency** once per minute

**Effect** You bend "divine" power to your will using the techniques taught you by the Razmiri priesthood. You grant a single target you touch a number of temporary Hit Points equal to twice your level that last for 24 hours. If the target was [[Unconscious]], it regains consciousness and doesn't lose consciousness again due to Hit Point loss as long as it has temporary Hit Points from this effect remaining.

> [!danger] Effect: Call Upon Razmir's Benevolence

**Source:** `= this.source` (`= this.source-type`)
