---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 25}"
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

*Resurrection tea* was named for its repugnant taste, said to be "strong enough to kill the living," and its incredible medicinal properties "powerful enough to raise the dead." The primary ingredients in this medicinal tea are ginseng and jujubes, enhanced with additional herbs, shaved deer antlers, sugi tree bark, and a variety of mushrooms stewed for several hours in a large pot to form a brown, pulpy, and viscous liquid. The bitterness and earthy taste make the tea rather unappetizing. The tea restores @Damage[(2d8+5)[healing]] Hit Points, and you reduce the DC of recovery checks by 1 for 8 hours.

> [!danger] Effect: Resurrection Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The tea reduces the DC of recovery checks by 3.

**Source:** `= this.source` (`= this.source-type`)
