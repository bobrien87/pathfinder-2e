---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Consumable]]", "[[Expandable]]", "[[Magical]]"]
price: "{'gp': 6}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When activated, this miniature transforms into a seemingly mundane sparrow. The sparrow flies to a destination of your choice within 200 feet that you can see, then Seeks in a @Template[type:burst|distance:30] using your Perception modifier before returning. The sparrow then unravels into a small map of the area it perceived, including any creatures it saw. The map is rudimentary and doesn't reveal anything the sparrow failed to perceive.

**Source:** `= this.source` (`= this.source-type`)
