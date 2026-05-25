---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]", "[[Poison]]", "[[Shove]]"]
price: "{'gp': 2800}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The putrid stench emanating from the catoblepas antlers adorning this *+2 greater striking Greater Crushing maul* interferes with your sense of smell. While wielding this weapon, you gain a +2 item bonus to saves against olfactory effects.

**Activate—Vile Stench** `pf2:1` (manipulate, olfactory)

**Requirements** Your last action was a successful Strike with the *catoblepas maul*

**Effect** The target must succeed at a DC 30 [[Fortitude]] save or become [[Sickened]] 1 (plus [[Slowed]] 1 for as long as it's sickened on a critical failure). A creature that succeeds at its save becomes temporarily immune to Vile Stench for 1 minute.

**Craft Requirements** The initial raw materials must include antlers from a catoblepas.

**Source:** `= this.source` (`= this.source-type`)
