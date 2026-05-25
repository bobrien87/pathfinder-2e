---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 80, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small metal fife is of extraordinary fine quality, with gold filigree on the embouchure. A fife of the faithful grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Call to Arms** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You play a rousing tune on the fife that carries across the battlefield. You and all allies in a @Template[type:emanation|distance:60] gain a +1 status bonus to saving throws for 1 round.

> [!danger] Effect: Call to Arms

**Source:** `= this.source` (`= this.source-type`)
