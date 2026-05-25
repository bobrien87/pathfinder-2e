---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Kickback]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Built from the larynx of a terror shrike, or similar animal that possesses a frightening screech or similar special ability, a *screech shooter* is a special *+1 striking harmona gun* designed to fire terrifying blasts of sound. A *screech shooter* deals sonic damage but can otherwise be used like a normal harmona gun.

**Activate—Screech Shot** `pf2:2` (emotion, manipulate, mental)

**Frequency** once per hour

**Effect** The screech shooter unleashes a frightening wail. All creatures in a @Template[type:emanation|distance:30] from you must attempt a DC 25 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Craft Requirements** The initial raw materials must include the larynx of a creature with a frightening screech.

**Source:** `= this.source` (`= this.source-type`)
