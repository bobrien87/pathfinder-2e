---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 3}"
usage: "worneyepiece"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This heavy set of mechanical goggles contains a variety of different lenses for different situations, including lenses that filter light at different intensities and frequencies and even some that capture heat and other stimuli. Clockwork mechanisms can swap between the lenses rapidly as needed. However, many of these lenses can only capture a single stimulus once and then are forever etched with it, making them unsuitable for long-term use.

When activated, the clockwork mechanism on the goggles rapidly switches between the different lenses, granting you low-light vision for 10 minutes.

> [!danger] Effect: Clockwork Goggles

**Source:** `= this.source` (`= this.source-type`)
