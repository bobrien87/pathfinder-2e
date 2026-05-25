---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Earth]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "worn"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *polished pebble aeon stone* imbues you with the strength of the earth, granting a +1 item bonus to saves and DCs against attempts to grapple or swallow you.

The stone's resonant power allows you to cast [[Grease]] as a primal innate spell once per day. You can target only surfaces, not objects, with this spell.

**Source:** `= this.source` (`= this.source-type`)
