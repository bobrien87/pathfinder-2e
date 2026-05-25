---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you Activate a smoke fan, it creates a cloud of colored smoke. The smoke fills a 5-foot radius. The creator chooses the smoke's color when creating the smoke fan. Creatures within the smoke's area are [[Concealed]], and all other creatures are concealed to them. The smoke lasts for 1 minute or until dissipated by a strong wind.

**Source:** `= this.source` (`= this.source-type`)
