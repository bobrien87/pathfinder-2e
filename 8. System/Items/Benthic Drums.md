---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]"]
price: "{'gp': 14000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large bass drum is made of driftwood and whale hide, with swirling shapes that hint at more distinct and sinister forms carved on its surface. This drum grants you a +2 item bonus to Performance checks while playing music with the instrument. You can communicate basic ideas with whales and other large sea animals by playing music with this instrument.

**Activate—Call from the Depths** `pf2:3` (concentrate, emotion, fear, manipulate, mental, sonic)

**Frequency** once per week

**Effect** You drum a song of an ancient creature, calling forth the cries of a great whale in the minds of your foes. All enemies in a @Template[type:emanation|distance:60] take @Damage[9d10[sonic]|options:area-damage,inflicts:frightened|traits:concentrate,emotion,fear,manipulate,mental,sonic] damage (DC 36 [[Will]] save). Creatures who fail are also [[Frightened]] 1.

**Source:** `= this.source` (`= this.source-type`)
