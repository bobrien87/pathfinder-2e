---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Emotion]]", "[[Fear]]", "[[Invested]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 15000}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When tied over your eyes, this ragged strip of black linen gives you a +3 item bonus to Intimidation checks and darkvision. You can see through the blindfold, but only using darkvision.

The first time a particular creature sees you in a day, it must succeed at a DC 37 [[Will]] save or be [[Frightened]] 1. This is an emotion, fear, and mental effect, and your allies become immune to it after about a week.

**Activate—Visions of Terror** `pf2:f` (concentrate)

**Frequency** once per minute

**Trigger** You damage a creature with a Strike

**Effect** Your target is gripped by intense fear. This has the effect of a DC 37 *vision of death* spell. The creature is then temporarily immune for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
