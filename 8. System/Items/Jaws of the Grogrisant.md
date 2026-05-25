---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Primal]]"]
price: "{'gp': 15000}"
usage: "worncirclet"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The teeth that fell off the Mantle of the Grogrisant were given to the scholars of Houses Fahlspar, Lotheed, Nicodemius, and Zespire, who—after much heated discussion—created this regal circlet. You gain a +3 item bonus to Diplomacy and Intimidation skill checks and [[Sense Motive]] checks against creatures that have the primal trait. When you invest in the headband, you either increase your Wisdom modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate—Primal Empathy** `pf2:2` (concentrate, mental)

**Frequency** once per hour

**Effect** You gain the ability to communicate with nature as if you were a part of it. You cast [[Telepathy]] at 6th rank, which can only be used to communicate with creatures that have the primal trait.

**Source:** `= this.source` (`= this.source-type`)
