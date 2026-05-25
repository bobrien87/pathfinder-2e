---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 360}"
usage: "worn"
bulk: "—"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The flower that adorns this hairpin is a blooming lotus flower that varies in color; it regrows in a day after the item is activated. Whether or not the hairpin's flower is in bloom, as long as you wear it and it's invested, it grants a +1 item bonus to Diplomacy checks.

**Activate—Scatter Petals** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You pluck the flower from the hairpin and scatter the petals, creating a flurry of color in a @Template[type:burst|distance:10] centered on you. You become [[Concealed]] for 1 minute or until you move from your current location. Any creature within the @Template[type:burst|distance:10] when you Activate the Item must succeed at a DC 23 [[Reflex]] save or become [[Dazzled]] until the end of its next turn (or [[Blinded]] until the end of its next turn on a critical failure). The flower blooms again the next day.

**Source:** `= this.source` (`= this.source-type`)
