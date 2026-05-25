---
type: item
source-type: "Remaster"
level: "0"
price: "{'gp': 5}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Simple blinds consist of a series of poles with a cloth to cover them. The cloth covering is styled to represent the natural surroundings such as green and brown leaf and wood patterns for forests, or gray rocks for underground environments. This cloth is either sheer enough to be seen through on one side, or sometimes has small slits cut in it, allowing someone behind it to see what is going on outside while remaining [[Hidden]]. While not the most convincing camouflage, it's good enough to fool many animals and creatures with lower intelligence.

Animal blinds take 1 minute to set up. Up to two Medium creatures or one Large creature may use the blinds at the same time. You can [[Take Cover]] behind the blind to gain standard cover. If the environment matches the terrain depicted on the blind, your circumstance bonus on Stealth checks to [[Hide]] increases to +4.

> [!danger] Effect: Animal Blind

**Source:** `= this.source` (`= this.source-type`)
