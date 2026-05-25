---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 7000, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This snare drum and sticks are made from dark wood, and the skin is fine antelope hide. This drum grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Prestissimo** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You play the snare with an extreme cadence. You and all allies within a @Template[type:emanation|distance:30] gain the [[Quickened]] condition until the end of your next turn and can use the extra action each round for only Step and Stride actions.

**Activate—Larghissimo** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You play the snare with a lassitude that drains the speed from your foes. Enemies within a @Template[type:emanation|distance:30] must attempt a DC 34 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature [[Slowed]] 1 for 1 round.
- **Failure** The creature is [[Slowed]] 2 for 1 round.
- **Critical Failure** The creature is slowed 2 and [[Off Guard]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
