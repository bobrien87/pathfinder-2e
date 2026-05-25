---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Spirit]]"]
price: "{'gp': 450}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Astral* weapons command powerful spiritual energy from the Astral Plane. This rune has the same effects as a *[[Ghost Touch]]* rune, plus Strikes with it deal an extra 1d6 spirit damage. If used to attack a creature that's possessing another creature, this weapon deals no damage to the possessed creature. On a critical hit against a creature possessing another creature, the possessing creature must succeed at a DC 26 [[Will]] save or be expelled and unable to possess a creature for 1d4 rounds.

**Source:** `= this.source` (`= this.source-type`)
