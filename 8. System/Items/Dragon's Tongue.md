---
type: item
source-type: "Remaster"
level: "11"
price: "{'gp': 1350}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 striking longspear* was crafted by a renowned monster hunter, who designed the prototype from the bones and scales of a diabolic dragon. The drathyrican folds of a young dragon, the organ that generates their magical breath, are crucial to the operation of the spear. The mechanics of the weapon are largely based on an injection spear: when the safety is disengaged and a secondary lever is squeezed, it produces a magical effect like a dragon's breath from the hollow tip of the spear.

**Activate—Breath of the Spear** `pf2:2` (concentrate, manipulate) The dragon's tongue releases a burst of energy that manifests as a @Template[type:cone|distance:30] dealing @Damage[6d6[untyped]|options:area-damage] damage with a DC 28 [[Reflex]] save. You can't use this activation again for 1d4 rounds. The damage type matches the breath of the dragon the weapon was made from, and this activation has the corresponding trait.

**Craft Requirements** The initial raw materials must include the drathyrican folds of a dragon.

**Source:** `= this.source` (`= this.source-type`)
