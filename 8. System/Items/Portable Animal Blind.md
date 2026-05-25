---
type: item
source-type: "Remaster"
level: "2"
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Simple blinds consist of a series of poles with a cloth to cover them. The cloth covering is styled to represent the natural surroundings such as green and brown leaf and wood patterns for forests, or gray rocks for underground environments. This cloth is either sheer enough to be seen through on one side, or sometimes has small slits cut in it, allowing someone behind it to see what is going on outside while remaining [[Hidden]]. While not the most convincing camouflage, it's good enough to fool many animals and creatures with lower intelligence.

Portable blinds are made of a wooden frame with camouflage material stretched over them, resembling a large kite. A hole in the center allows for a one-handed ranged weapon to be fired without obstruction. A single person can use the [[Take Cover]] action while carrying a portable blind. When you do so, you gain a +2 circumstance bonus to Stealth checks to [[Hide]] instead of the normal benefits of standard cover.

> [!danger] Effect: Portable Animal Blind

**Source:** `= this.source` (`= this.source-type`)
