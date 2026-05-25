---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 9}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

**Activate** `pf2:1` (concentrate)

Strange striations and pits mark the head of a ranging shot. When the activated ammunition is fired, it sends out whistling pings along its path until it hits something or reaches its maximum range. As long as you can perceive the sounds the ammunition makes, you can tell exactly how far it has flown. The sounds are audible to creatures who didn't Activate the ammunition, but they receive no special information from the ranging shot's whistling.

**Source:** `= this.source` (`= this.source-type`)
