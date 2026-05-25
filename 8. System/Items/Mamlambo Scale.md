---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 990}"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The faint glow beneath the thick, algae-green scales of this suit of *+1 resilient scale mail* hints at the armor's source.

**Activate—Luminous Lure** `pf2:1` (concentrate, light, manipulate, mental, visual)

**Frequency** Once per day

**Effect** The *mamlambo scale* sheds dim light in a 20-foot emanation. The light has a duration of 1 minute, but you can extinguish the light with an Interact action. A creature that begins its turn in the light must attempt a DC 26 [[Will]] save. Regardless of the save's result, the creature is temporarily immune for 1 hour.

> [!danger] Effect: Luminous Lure
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Slowed]] 1 for 1 round.
- **Failure** The creature is [[Fascinated]], and for as long as it remains in the light, it must spend at least 1 of its actions on each of its turns to move closer to the source of the light. If the creature ends its movement adjacent to you, it is slowed 1 until it is out of the light or until you make a Strike against it.
- **Critical Failure** As failure, but the creature is also [[Off Guard]] against the first Strike you make against it while it is slowed.

**Craft Requirements** The initial raw materials must include the scales and hide of a mamlambo.

**Source:** `= this.source` (`= this.source-type`)
