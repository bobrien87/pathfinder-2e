---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 650, 'pp': 0, 'sp': 0}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fine copper kettledrum has a dark skin stretched over it, and the tension rods are stained a dark red. This drum grants you a +2 item bonus to Performance checks while playing music with the instrument.

**Activate—Sustain Dread** `pf2:1` (auditory, emotion, fear, manipulate, mental)

**Frequency** once per day

**Effect** You beat a march on the timpani that continuously increases in tempo. Enemies within a @Template[type:emanation|distance:30] must attempt a DC 26 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The target can't reduce its frightened value below 1 for 1 round.
- **Failure** The target can't reduce its frightened value below 1 for 1 minute.
- **Critical Failure** As failure, and it becomes [[Frightened]] 1.

**Source:** `= this.source` (`= this.source-type`)
