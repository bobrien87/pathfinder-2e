---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2600}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The main portion of this set of bagpipes is fashioned from the dried skin of a cauthooj, with the feathers still attached. The bird's vocal cords are crafted into the instrument's reeds. The pipes grant a +2 item bonus to Performance checks while playing music with them.

**Activate—Disorienting Fugue** `pf2:2`(auditory, incapacitation, manipulation, mental)

**Frequency** once per hour

**Effect** You play several notes on the pipes, quickly altering their pitch and tone. Each creature within a @Template[emanation|distance:20] must attempt a DC 31 [[Will]] save to resist the song. Creatures that attempt this save become temporarily immune to Disorienting Fugue for 1 minute.
- **Critical Success** The target is unaffected and its temporary immunity to Disorienting Fugue increases to 1 hour.
- **Success** The target is unaffected.
- **Failure** The target is [[Confused]] for 1 round.
- **Critical Failure** The target is confused for 1 round and immediately attacks itself (in the normal fashion for attacking oneself while confused). This Strike doesn't give the creature a flat check to recover from the confusion.

**Activate—Throw Song** R (auditory, mental)

**Trigger** A creature within 30 feet attempts a melee Strike against you or an ally

**Effect** You let loose a staccato chirp from the pipes that appears to come from somewhere else. The triggering creature must attempt a DC 31 [[Will]] save. On a failure, the creature redirects the Strike to another creature of your choice within reach of the melee Strike. If no other creatures are within range, the affected creature instead takes a –2 penalty to the Strike.

**Craft Requirements** The initial raw materials must include the skin and vocal cords of a cauthooj.

**Source:** `= this.source` (`= this.source-type`)
