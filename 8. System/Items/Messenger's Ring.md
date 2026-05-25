---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver signet ring changes to match the insignia of a lord or organization you serve (or your own face, if you serve no one else). It grants you a +2 item bonus to Diplomacy checks and lets you cast [[Message]] as an arcane innate spell at will.

**Activate—Dispatch Messenger** 1 minute (concentrate)

**Frequency** once per day

**Effect** The ring casts [[Animal Messenger]] to your specification. The animal is a magical creature that springs from the ring, and its appearance suits the iconography or heraldry of the lord or organization represented by the ring.

**Source:** `= this.source` (`= this.source-type`)
