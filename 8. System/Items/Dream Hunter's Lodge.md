---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Dream]]", "[[Magical]]", "[[Mythic]]", "[[Structure]]"]
price: "{'gp': 13500}"
usage: "other"
bulk: "L"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This miniature hunter's lodge fits comfortably into the palm of one's hand.

**Activate–Expand Lodge** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You set the lodge on the ground, where it expands into a structure 40 feet long, 20 feet wide, and 20 feet high. The lodge is well-built, with a sturdy stone foundation, thick timber walls, and a peaked roof shingled with scraps of bark. The lodge's ground floor contains a dining hall on one end and a sitting area with a hearth surrounded by comfortable chairs on the other. A staircase connects the hall to the lodge's second floor, which consists of four simply furnished bedrooms. The lodge is decorated throughout with taxidermic beasts native to the Dimension of Dreams. If a creature inside the lodge spends 10 minutes studying these trophies, they gain a +3 item bonus to the next skill check they make in the next 24 hours to [[Recall Knowledge]] about any creature with the dream trait. Furnishings or decorations removed from the lodge disappear but return to their original locations inside the lodge with the next activation.

You can Dismiss the dream hunter's lodge to return it to its miniature form.

**Activate–Oneiric Expedition** 10 minutes (concentrate)

**Frequency** once per day

**Requirements** The dream hunter's lodge has been expanded and you are inside

**Effect** Spend 1 Mythic Point. You and all creatures inside the lodge fall into a magical slumber, and the lodge disappears from existence. After 8 hours, the lodge reappears in the Dimension of Dreams (or in the Universe, if the lodge was already in the Dimension of Dreams), as if transported there by an [[Interplanar Teleport]] spell. Upon arrival, creatures inside the lodge awaken, fully rested (but this effect does not increase the number of times per day you can do your daily preparations).

**Source:** `= this.source` (`= this.source-type`)
