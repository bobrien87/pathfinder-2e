---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

*Spiritsight tea* exudes a soft blue glow, creating illumination equal to that of a candle. When consumed, your eyes take on a soft glow as well, and you can see [[Invisible]] creatures and objects for 10 minutes; such creatures appear to you as translucent shapes, and they're [[Concealed]] to you. You gain a +1 item bonus to Perception checks to [[Seek]] incorporeal creatures.

> [!danger] Effect: Spiritsight Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The duration of being able to see invisible creatures and objects increases to 30 minutes, and the duration of the item bonus increases to 8 hours.

**Source:** `= this.source` (`= this.source-type`)
