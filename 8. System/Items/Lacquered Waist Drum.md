---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1300}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hourglass-shaped drum has two heads, each of which produces a different sound when struck. When played together, the resonance of the two sounds is effective in repelling evil spirits. This drum can be played as an instrument, granting a +2 item bonus to Performance.

**Activate—Memories of Life** `pf2:2` (concentrate, manipulate, vitality)

**Frequency** once per hour

**Effect** You play both heads of the drums, generating a pulse of energy that targets one creature within 30 feet that has the undead trait. This deals 5d8 vitality damage (DC 28 [[Fortitude]] save) to that creature; if the undead also has the ghost trait, the ghost becomes [[Sickened]] 1 if it fails the save.

**Activate—Memories of Joy** `pf2:3` (concentrate, manipulate, vitality)

**Frequency** once per hour

**Effect** You raucously play both heads of the drums, accompanied with shouting and dancing. This display generates a pulse of energy in a @Template[type:emanation|distance:30] from you. All undead creatures within this area must attempt a DC 28 [[Fortitude]] save.
- **Critical Success** The creature takes no damage.
- **Success** The creature takes 2d8 vitality damage. Failure The creature takes 5d8 vitality damage; if the creature has the ghost trait, it becomes [[Stupefied 1]] for 1 minute.
- **Critical Failure** The creature takes 10d8 vitality damage; if the creature has the ghost trait, it becomes [[Stupefied 2]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
