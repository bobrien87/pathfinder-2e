---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This unassuming hooded lantern contains a mass of flash beetle eggs suspended in a magical solution. It sheds light on a 45-foot radius (and dim light in the next 45 feet).

**Activate—Spotlight** `pf2:1` (light, manipulate, visual)

**Frequency** once per day

**Effect** Flipping a concealed lever in the lantern's handle triggers a small current to pass through the solution. The eggs brighten and emit a series of brilliant flashes in a @Template[cone|distance:30]. Each creature in the area of effect must attempt a DC 18 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round.
- **Critical Failure** The creature is blinded for 1 minute.

**Craft Requirements** The initial raw materials must include the eggs of a flash beetle.

**Source:** `= this.source` (`= this.source-type`)
