---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Magical]]"]
price: "{'gp': 140}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Smaller than breath-powered bagpipes, the uilleann pipes are worked using a set of elbow bellows, and the pipes are made from finely carved bone. This bagpipe grants you a +1 item bonus to Performance checks while playing music with the instrument.

**Activate—Hand Chords** `pf2:2` (auditory, concentrate, manipulate)

**Frequency** once per day

**Effect** You execute a complex set of complementary arpeggios for dramatic effect. You and all allies within a @Template[type:emanation|distance:15] gain a +1 status bonus to the next attack roll, Perception check, saving throw, or skill check you attempt before the end of your next turn. Each target chooses which roll to use the bonus on before rolling.

> [!danger] Effect: Hand Chords

**Source:** `= this.source` (`= this.source-type`)
