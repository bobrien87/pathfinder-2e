---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Mythic]]", "[[Occult]]"]
price: "{'gp': 14000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This foot-long, spindle-shaped puzzle box is made of otherworldly metal inlaid with a finely traced labyrinth pattern. By manipulating the key's length, the wider spindle can be caused to open, unfold, and move up and down along the shaft, often in ways that defy geometry.

Every spindle key is attuned to one of the prison-spires that float above the Oubliette Plains in the Dreamlands. As a 10-minute activity, a creature can solve a spindle key by attempting a DC 37 [[Occultism]] check. On a success, that PC can thereafter use both of the spindle key's activations. On a critical failure, the key's magic plays havoc with the creature's spatial awareness. The creature becomes [[Clumsy]] 1 for 24 hours (which can't be reduced by any means) and can't attempt to solve the spindle key again until the effect ends.

**Activate—Align Spindle** `pf2:2` (concentrate, manipulate, occult)

**Effect** You rotate the sections of the spindle key into an arrangement of your liking. As you do, the corresponding steel separators between floors of Liralarue's Oubliette spin to match that arrangement. If a creature is within the ten-foot-space between floors at this time, they take 10d6 bludgeoning damage (DC 37 [[Reflex]] save) from being crushed and are then pushed into one of the adjoining rooms at random as the rotation seals it up.

**Activate—Breach** `pf2:2` (concentrate, manipulate, occult)

**Frequency** once per hour

**Effect** You harness the key's occult geometry to bypass a lock within 30 feet. You attempt to Pick the Lock, using Occultism instead of Thievery for the check. You can spend a Mythic Point to attempt the check at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
