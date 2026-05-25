---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 38000}"
usage: "worncloak"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magical cloak was crafted from the feathers and scales of a legendary giant fish that could transform into a resplendent bird.

**Activate—Cut Air and Sea** `pf2:1` (concentrate, manipulate)

**Effect** The cloak ripples, becoming either giant eagle feathers or iridescent fish scales. Until you next Activate the cloak, you gain either a swim Speed of 60 feet and the ability to breathe underwater or a fly Speed of 40 feet.

**Source:** `= this.source` (`= this.source-type`)
