---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Designed for a frequent sponsor of theatrical productions who liked to stay informed of all the off-stage drama, these silver opera glasses are affixed to a slender redwood handle. They can't be worn on the face but must be raised to the eyes and held there, at which point the spectacles of discernment grant a +2 item bonus to Perception checks to notice details at a distance.

**Activate—Reveal the Truth** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You raise the spectacles to regard a target creature through them; the target must be within 60 feet. You immediately gain the ability to speak and understand the language the target creature is currently speaking, or its native language if it's not currently talking, for 24 hours. During this time, you can Interact with the spectacles of discernment to flip down a pair of supplementary lenses. When you do so, if you're observing the creature you originally targeted, roll a secret counteract check with a counteract modifier of +23 against any illusion, morph, or polymorph effect affecting the target, but only for the purpose of determining whether you see through the disguise or not.

**Source:** `= this.source` (`= this.source-type`)
