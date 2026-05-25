---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 12}"
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

This tea is brewed with a mixture of matcha, turmeric, and 10 drops of morning dew, creating a fragrant but mildly bitter tea. The bitter aftertaste is said to be the most important element of *longnight tea*, for it's believed that this flavor lingers on the tongue and aids in keeping you awake and alert. The tea is favored by scholars and soldiers alike, although the value to which each attributes the ability to endure long nights without sleeping varies—and is often the subject of unusually impassioned debate. When you drink *longnight tea*, it grants you a +1 item bonus to saving throws against sleep effects for 1 hour.

> [!danger] Effect: Longnight Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The duration increases to 8 hours, and the tea removes the [[Fatigued]] condition.

**Source:** `= this.source` (`= this.source-type`)
