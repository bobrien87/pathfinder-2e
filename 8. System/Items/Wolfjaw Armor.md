---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Primal]]"]
price: "{'gp': 355}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Barbarians, druids and other outlanders are often forced to spend the harsh winter months protecting their communities from one of the deadliest predators to stalk the forests and taiga of the northern reaches, the fearsome witchwarg. This *+1 hide armor* is assembled from the hide and fur of a trio of witchwargs, and it conveys on the wearer both an attack akin to the witchwargs' deadly jaws and the ability to channel the frigid cold of the witchwarg's Winter Breath.

**Activate** `pf2:2` (cold, manipulate)

**Frequency** once per day

**Effect** You breathe a cloud of frost in a @Template[cone|distance:15] that deals 5d8 cold damage (DC 23 [[Reflex]] save).

**Activate** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You gain a jaws unarmed attack that you make using your hands. This attack deals 1d8 piercing damage plus 1 cold damage, is in the brawling group, and has the trip and unarmed traits.

> [!danger] Effect: Wolfjaw Armor

**Craft Requirements** The initial raw materials must include the hides of at least three witchwargs.

*Note: A duration for the activation effect was not included in the statblock by Paizo. We have assumed a 1 minute duration for the effect*

**Source:** `= this.source` (`= this.source-type`)
