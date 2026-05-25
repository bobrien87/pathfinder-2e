---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 320}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This complex clockwork outerwear, worn over armor or other clothing, is composed of thin, interlocking scales of myriad colors attached to numerous clockwork gears that can rotate between all visible colors and shades. When activated, the clockwork gears work double-time to temporarily switch and adjust the scales to match the exact coloration of the area around you, allowing you to blend in as long as you stay still. For 1 hour, you can Hide without needing cover or concealment to do so. This doesn't allow you to [[Sneak]] without ending your movement in cover or concealment, however, as the clockwork flips over and adjusts the scales to match your background as you move, giving the impression of rippling waves of color and revealing your movement. Once the duration expires, the overworked clockwork and scales fall apart.

**Source:** `= this.source` (`= this.source-type`)
