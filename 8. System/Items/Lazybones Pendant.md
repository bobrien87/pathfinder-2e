---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 130}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A lazybones pendant is a six-sided die pendant carved from the regretful bones of Work-Too-Hard Whappa, a goblin unusually industrious in life and said to be making up for a long-overdue rest in his afterlife. Depicted on the five sides of this six-sided die are representations of Whappa engaged in various acts of slothful mischief, while the remaining side is utterly blank; apparently, he's so engrossed in his indolence that even his image has forgotten to show up on that side of the die.

When you wear and invest in this pendant, you gain a +1 item bonus to checks when you Follow the Expert.

**Activate—Can't Someone Else Do It?** `pf2:3` (concentrate, manipulate, occult)

**Frequency** once per day

**Effect** You cast [[Phantasmal Minion]], summoning an ephemeral version of yourself. When you Activate the pendant and each time you Sustain the spell, your phantasmal minion gains a reaction that can be used only to Aid an ally. It uses your skills for any skill checks and can't Aid an attack.

**Source:** `= this.source` (`= this.source-type`)
