---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 145, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This finely crafted set of bagpipes bears the hallmark scratches and wear of the battlefield, but it nonetheless shines with polish and has been played with love. These bagpipes grant you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Inspirational Salute** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You tap into the great music of the pipes, inspiring all allies who can hear. You and all allies within a @Template[type:emanation|distance:60] gain a +1 status bonus to damage rolls and saves against fear effects for 1 minute.

> [!danger] Effect: Inspirational Salute

**Source:** `= this.source` (`= this.source-type`)
