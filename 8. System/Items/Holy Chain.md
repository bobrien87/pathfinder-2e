---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Divine]]", "[[Holy]]", "[[Invested]]", "[[Noisy]]"]
price: "{'gp': 2500}"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+2 resilient chain mail* is made of fine white links of a strange and slightly translucent pale metal, and the sleeves and skirt are fashioned into smaller trails that resemble feathers. Unlike normal chain mail, *holy chain* has no Speed reduction, its armor check penalty is 0, and its Bulk is 1.

You gain a +1 circumstance bonus to AC and saving throws against fiends. You appear radiant while you wear the armor, giving you a +2 item bonus to Diplomacy checks against all creatures except fiends.

If you're unholy, you're [[Drained]] 2 while wearing *holy chain*. You can't recover from this condition while wearing the armor.

**Activate—Celestial Flight** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The armor sprouts glowing wings that grant you a fly Speed of 30 feet. The wings shed bright light in a 40-foot radius (and dim light to the next 40 feet). The wings fade away after 10 minutes.

> [!danger] Effect: Holy Chain

**Craft Requirements** You're holy.

**Source:** `= this.source` (`= this.source-type`)
