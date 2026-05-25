---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Thrown 10]]"]
price: "{'gp': 225}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This spine and skull of a slain hydra has been picked clean by a carrion bird and crafted into this *+1 striking club*. In addition to its normal traits, the *hydra head club* also has the modular P trait, as it can be manipulated to cause the jaws to spring open. Even in death, its head twitches independently. The creature's famed regenerative powers are still present, despite the creature's death; if damaged, the *hydra head club* repairs itself at the rate of 1 Hit Point per minute, unless it has been completed destroyed.

**Activate—Reactive Snap** `pf2:f` (attack)

**Frequency** once per day

**Trigger** You attempt a Strike as a Reaction

**Effect** The *hydra head club* snaps with a momentary burst of its former glory. Your Strike attempt deals an additional 1d6 damage. If your Strike misses, the activation does not count against the *hydra head club's* activation frequency.

**Craft Requirements** You must supply a skull and spine of a hydra when crafting this weapon.

**Source:** `= this.source` (`= this.source-type`)
