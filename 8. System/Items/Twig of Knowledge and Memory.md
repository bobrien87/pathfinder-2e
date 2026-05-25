---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Plant]]"]
price: "{'gp': 4}"
usage: "held-in-1-hand-hung-on-a-cord-or-attached-to-clothing"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This tiny magic item looks like a twig from the rare mti'le tree with its swirls of reddish-gold veins through dark brown wood. Each one is unique and fits easily in the palm of a Medium-sized creature's hand. When pressed to the temple or lips of a sentient creature, that creature can immediately attempt a check to Recall Knowledge about any subject using a corresponding skill (such as Society to Recall Knowledge about a humanoid); they gain a +1 status bonus on this check. This consumable is not immediately consumed on its first use, but can be used three times before it loses its power and becomes a mundane, if still beautiful, twig.

**Source:** `= this.source` (`= this.source-type`)
