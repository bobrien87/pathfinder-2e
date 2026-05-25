---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 140, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ash recorder is highly polished, with a spiral, serpentine pattern etched along its length. The recorder grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Sooth Serpents** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You play a swift composition that fascinates all snakes, pythons, vipers, and serpents that hear it. At the GM's discretion, creatures with major serpentine features, such as serpentfolk, are also subjected to this effect. All such creatures within a @Template[type:emanation|distance:30] must attempt a DC 20 [[Will]] save.
- **Critical Success** The target's attitude toward you decreases by one step.
- **Success** The creature is unaffected.
- **Failure** The target's attitude toward you improves by one step, and it feels a powerful urge to dance. It takes a –5-foot penalty to its Speeds for 1 minute as it sways and dances to the music.
- **Critical Failure** As failure, but the target's attitude toward you improves by two steps.

> [!danger] Effect: Sooth Serpents (Speed Penalty)

**Source:** `= this.source` (`= this.source-type`)
