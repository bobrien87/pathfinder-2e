---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 7000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This blasphemous idol has the vague outline of a recumbent humanoid, but the more detail one perceives, the more its alien nature is revealed. The mere presence of the effigy causes disturbing dreams, and anyone who sleeps within 50 feet of the item must succeed at a DC 30 [[Will]] save or awaken [[Fatigued]].

**Activate—Whispers of Leng** 10 minutes (auditory, manipulate)

**Frequency** once per day

**Effect** You whisper a name and whatever details you recall about that person to the effigy, telling it everything you can about your target. The next time the target sleeps, they are subject to a [[Nightmare]] spell (DC 30). This continues every time the target sleeps until they die, you whisper a new target to the effigy, or the target gets a critical success on their save against the nightmare.

**Activate—Smothering Lassitude** `pf2:2` (concentrate, manipulate, visual)

**Frequency** once per day

**Effect** You brandish the effigy aloft, exposing all who see it to its bizarre visage. You and all creatures within a @Template[type:emanation|distance:120] must attempt a DC 34 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Stupefied 1]] until the start of your next turn.
- **Failure** The creature is stupefied 1 and [[Stunned]] 1 until the start of your next turn.
- **Critical Failure** The creature is [[Stupefied 2]] and stunned 1 until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
