---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 10]]", "[[Unholy]]", "[[Versatile s]]"]
price: "{'gp': 60000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This slim *+3 major striking unholy wounding dagger* has a curved blade akin to that of a peeling knife. Soft elf-leather strips adorn the handle. If you are a demon, it amplifies any auras you have by granting a +1 item bonus to your aura's DCs.

**Activate—Burrowing Splinter** `pf2:1` (manipulate)

**Frequency** one per day

**Requirements** Your previous action was a successful Strike with the *apotheosis knife*

**Effect** You twist the blade, causing a sliver of the dagger to break off inside the body of the creature you damaged with the *apotheosis knife* on your prior action. Just as the blade itself cuts away flesh, this splinter slices away at the target's mind. The target must attempt a DC 43 [[Will]] save. If the target is a demon, the burrowing splinter automatically triggers the effects of their sin vulnerability, regardless of their saving throw result.
- **Critical Success** The target takes no additional damage.
- **Success** The target takes 6d6 mental damage and is [[Stupefied 1]] until the end of their next turn.
- **Failure** The target takes 6d6 persistent,mental damage and is stupefied 1 with an unlimited duration.
- **Critical Failure** The target takes 12d6 persistent,mental damage, is stupefied 1 with an unlimited duration, and is [[Stunned]] 3.

**Source:** `= this.source` (`= this.source-type`)
