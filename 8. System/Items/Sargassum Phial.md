---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]", "[[Incapacitation]]", "[[Mental]]", "[[Poison]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A layer of vapor swirls just below the surface of this glass container holding a large, dried heap of fungal-encrusted seaweed. You can throw the phial up to 30 feet when you Activate it. When opened or thrown, a Medium sargassum heap effigy reconstitutes to release a hallucinogenic cloud in a @Template[emanation|distance:15], forcing each creature to attempt a DC 20 [[Fortitude]] save. On a failure, a creature rolls 1d4 rounds (unless otherwise noted). At the beginning of their turn, an affected creature attempts a new save.

**1** The target thinks they are sinking through the floor. It falls [[Prone]] and spends 1 action on its next turn flailing its limbs as if attempting to swim.

**2** The target thinks an item they are holding turns into a viper. The target Releases the item and spends its next turn [[Fleeing]] from it.

**3** The target thinks they have shrunk to 1/10 their normal size. For 1 round, it is [[Slowed]] 2, [[Enfeebled]] 2, and takes a –10-foot status penalty to its Speed.

**4** The target believes they are melting. It drops everything it's holding and becomes slowed 2 and [[Clumsy]] 2 for 1 round.

**Craft Requirements** Supply the corpse of a sargassum heap.

**Source:** `= this.source` (`= this.source-type`)
