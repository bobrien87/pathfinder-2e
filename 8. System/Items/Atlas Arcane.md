---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This well-worn vellum scroll has edges trimmed with golden thread, and it unrolls to reveal a map of the nearby area. The atlas arcane always shows the surrounding area (out to a 36-mile radius centered on the map) with a reasonable level of detail, providing a +1 item bonus to Survival checks and any skill checks to [[Recall Knowledge]], provided the checks are related to the location detailed on the map.

**Activate—Situation Report** `pf2:3` (auditory, concentrate, detection, manipulate)

**Frequency** once per day

**Effect** You speak a command phrase, and the map reveals the location of all troop movements within the area it maps. This intel is current the moment the phrase is spoken but does not update afterward, and moving the map does not reveal further intel.

**Source:** `= this.source` (`= this.source-type`)
