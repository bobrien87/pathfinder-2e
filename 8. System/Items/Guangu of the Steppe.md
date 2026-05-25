---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 225, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large drum is made of hardwood and horse hide, with white silhouettes of coursing stallions along its circumference. This drum grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—The Hammer of Hooves** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You hammer a thundering beat on the guangu. For 10 minutes, mounted allies within a @Template[type:emanation|distance:60] gain a +10-foot status bonus to their mount's Speeds. They also gain a +1 status bonus to Nature checks to Command an Animal and automatically succeed when they Command an Animal they're mounted on to take a move action (such as Stride).

> [!danger] Effect: The Hammer of Hooves

> [!danger] Effect: The Hammer of Hooves (Mount Speed)

**Source:** `= this.source` (`= this.source-type`)
