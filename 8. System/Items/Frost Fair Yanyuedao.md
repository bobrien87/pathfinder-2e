---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Artifact]]", "[[Cold]]", "[[Deadly d8]]", "[[Forceful]]", "[[Reach]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *Frost Fair Yanyuedao* is a *+2 greater striking yanyuedao* (use statistics for glaive) once wielded by a legendary military general from Goka. This weapon was constructed from pieces harvested from a dragon's body. When in an area of severe cold or colder, the *Frost Fair Yanyuedao* becomes a *+3 major striking yanyuedao* with a glowing blue cutting edge and the following ability.

**Activate—Dragon Chill** `pf2:1` (manipulate)

**Effect** Until the end of your turn, the *Frost Fair Yanyuedao* gains the effects of a *Greater Frost* rune. While under this effect, if you critically succeed at a Strike using this weapon against a creature who has resistance or immunity to cold, that creature must attempt a DC 31 [[Fortitude]] save or be [[Slowed]] 1 for 1 minute.

> [!danger] Effect: Dragon Chill

**Source:** `= this.source` (`= this.source-type`)
