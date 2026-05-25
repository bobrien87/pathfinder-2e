---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Invested]]", "[[Occult]]"]
price: "{'gp': 1750}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This cloak flows, covering and concealing the wearer's body. The cloak allows you to cast [[Figment]] as an occult innate cantrip. Although naturally a dull gray, while invested the cloak picks up colors and patterns from its surroundings, granting a +2 item bonus to Stealth checks.

**Activate—Draw Hood** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You draw the hood up and gain the effects of a 4th-rank [[Invisibility]], with the spell's normal duration or until you pull the hood back down, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
