---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 8500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted by archons for mortal use, this trumpet is made of luminous gold and ivory, giving off a soft glow that warms the soul. This trumpet grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Archon's Note** `pf2:1` (auditory, incapacitation, manipulate)

**Frequency** once per day

**Effect** You blast a note on the horn so clear and pure that its grandeur stuns your enemies and inspires your allies. Allies in the area gain a +1 status bonus to attack rolls and saving throws for 1 round. Enemies within a @Template[type:emanation|distance:60] must attempt a DC 35 [[Fortitude]] save saving throw. They're then temporarily immune for 1 day.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]] for 1 round.
- **Failure** The creature is [[Stunned]] 1 and off-guard for 1 round.
- **Critical Failure** The creature is [[Stunned]] 2 and off-guard for 1 round.

**Source:** `= this.source` (`= this.source-type`)
