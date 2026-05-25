---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Concussive]]", "[[Magical]]", "[[Scatter 10]]"]
price: "{'gp': 15000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The larynx of a leydroth, a dangerous creature whose roar can unravel magic, is integrated into the firing mechanism of this *+3 greater striking blunderbuss*.

**Activate—Dispelling Blast** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The *leydroth spellbreaker* emits a @Template[cone|distance:30] of dispelling energy. Attempt a single counteract check at +25 against each spell or magical effect in the area, plus one item or effect on each creature in the area, with the effects of [[Dispel Magic]].

**Craft Requirements** The initial raw materials must include the larynx of a leydroth.

**Source:** `= this.source` (`= this.source-type`)
