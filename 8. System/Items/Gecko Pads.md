---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 25}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Gecko pads are thin, clockwork devices shaped like palms, which can be strapped onto existing handwear or a creature's hands. When activated, they whir to life and improve your grip on surfaces, while slowly releasing a sticky substance stored within the device's surface to help you climb. The pads give you a climb Speed equal to your Speed as long as your hands are free.

The climb Speed lasts for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
