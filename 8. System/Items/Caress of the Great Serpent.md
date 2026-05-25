---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Sweep]]"]
price: "{'gp': 24000}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater striking extending urumi* was fashioned after the legendary eightheaded orochi serpent, with its whiplike metal blades carved to resemble the many heads of the mythical beast, and its hilt wrapped in scaled leather. These weapons are commonly used by those who worship an orochi, raiding and threatening settlements to obtain sacrifices for the beast in hopes of being granted some modicum of its power.

**Activate—Serpent's Kiss** `pf2:3` (concentrate)

**Frequency** once per day

**Effect** You use your urumi as an effigy with which to call upon an orochi's power, offering your blood in exchange. You can make up to eight Strikes with a –2 penalty, each against a different target within 30 feet. For each Strike you choose to make, you take 1d6 piercing damage. Each attack counts toward your multiple attack penalty, but don't increase your penalty until you've made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
