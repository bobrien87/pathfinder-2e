---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Mental]]", "[[Oil]]"]
price: "{'per': 1, 'value': {}}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This pungent herbal ointment was originally only intended for use as an analgesic. That being said, popular folklore around this salve claims it can do anything from curing fevers to repelling vampires, a reputation that, if nothing else, is easy to get swept up in. When you activate a dose of panaceatic salve by rubbing it on your skin, you gain 4d8+10 temporary Hit Points for 10 minutes. At the end of this duration, if you still retain at least 1 of these temporary Hit Points, you can attempt a new saving throw against an ongoing disease or poison affliction you're afflicted with; if you fail or critically fail this saving throw, you don't increase the affliction's stage.

> [!danger] Effect: Panaceatic Salve

**Source:** `= this.source` (`= this.source-type`)
