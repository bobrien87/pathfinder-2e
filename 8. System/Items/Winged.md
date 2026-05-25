---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 2500}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune is a swirling glyph on the front of the armor. A large pair of transparent, ephemeral wings floats out from the back of the armor.

**Activate—Take to the Skies** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You trace the rune on the front of the breastplate, and the armor's ephemeral wings grow tangible, granting you a fly Speed of 25 feet or your land Speed, whichever is slower. This effect lasts for 5 minutes or until you Dismiss it. Once the effect ends, the wings disappear completely, reappearing in their ephemeral form 1 hour later

**Source:** `= this.source` (`= this.source-type`)
