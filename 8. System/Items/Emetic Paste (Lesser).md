---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Healing]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

[[Sickened]] creatures have difficulty swallowing, so you can Activate emetic paste by applying it to your skin or that of a sickened creature within reach, typically on the throat. The paste makes it easy for the sickened creature to purge, granting it an immediate Fortitude save to reduce its sickened condition. The paste grants the target a +2 item bonus to that save and to all saving throws to reduce the sickened condition for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
