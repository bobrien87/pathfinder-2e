---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 72}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:2` (concentrate)

Eyes are carved onto a sighting shot. When you Activate the ammunition, it glows, shedding bright light for 20 feet and dim light for 20 feet beyond that. If you shot the activated ammunition, your mind swirls with images of what the sighting shot passed and hit as if you sprinted along the ammunition's course. You see this path as if with your normal visual senses. Once a sighting shot hits anything or reaches its maximum range, it stops transmitting images to you. A sighting shot's light is visible to creatures who didn't Activate the ammunition, but they receive no special information from it.

**Source:** `= this.source` (`= this.source-type`)
