---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2000}"
usage: "worn"
bulk: "L"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This weighty brass disk is inscribed with the ancestral names of its previous owners and now includes your own. When worn, it rests against your chest with a heavy warmth, a reminder of the strength of those who came before you. While worn and invested, you gain a +2 item bonus to Will saves. This bonus increases to +3 if the effect has the fear trait.

**Activate—Strengthen Resolve** `pf2:1`

**Frequency** once per day

**Effect** You extend your resolve to your allies, casting [[Strength of Mind]] on up to three willing targets.

**Source:** `= this.source` (`= this.source-type`)
