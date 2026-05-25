---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 450}"
usage: "implanted"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An antenna with a bioluminescent lure protrudes from your head, drawing enemies' attention. When not activated, the antenna lays flat and blends in with your hair or skin.

**Activate—Raise Lure** `pf2:1` (manipulate, mental, visual)

**Frequency** once per day

**Effect** Until the beginning of your next turn, the lure raises above your head and lights up with multicolored flashes that draws creatures closer. Any creature that begins its turn within @Template[emanation|distance:20]{20 feet} of you must succeed at a DC 23 [[Will]] save or become [[Fascinated]] by the lure and must spend at least one of its actions to move toward you. The fascination ends at the end of the creature's turn.

**Source:** `= this.source` (`= this.source-type`)
