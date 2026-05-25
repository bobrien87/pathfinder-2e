---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Fire]]", "[[Light]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

These wafers contain ground-up alchemical reagents that activate shortly after being snapped. First popularized by technicians in Absalom's Ivy Playhouse, they have spread throughout Golarion as an inexpensive way to add to the visual splendor of a show without relying on magic. When you activate a spark wafer, you bend the wafer, nearly snapping it in two, and then throw it at a corner of a square within 20 feet (all part of the same manipulate action). The wafer then releases a 10-foot-high column of sparks for 1 round. The sparks shed bright light in a @Template[type:burst|distance:5] and dim light in the next 5 feet. Any creature that begins their turn in the burst takes @Damage[1d4[fire]|options:area-damage] damage (DC 14 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
