---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Apex]]", "[[Holy]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 40000}"
usage: "wornclothing"
bulk: "L"
source: "Pathfinder #206: Bring the House Down"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant toga is infused with inexhaustible energy to enjoy life possessed by azatas. You gain resistance to poison 20 and become immune to [[Deafened]]. When you invest in the robes, you either increase your Constitution score by 2 or increase it to 18, whichever would give you a higher score. If you are unholy, you become deafened while wearing the toga.

**Activate—Elysium's Gasp** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You are exposed to an inhaled poison

**Effect** Purifying gusts of sweet-scented air swirl around you, making you immune to inhaled poisons for 1 minute.

**Activate—Elysium's Breath** 1 minute (concentrate, healing)

**Frequency** once per day

**Effect** The air around the robe constantly circulates to keep you healthy. For 8 hours, you become immune to diseases spread via inhalation, olfactory effects, and environmental effects that would prevent you from breathing (including being underwater or from being strangled).

**Source:** `= this.source` (`= this.source-type`)
