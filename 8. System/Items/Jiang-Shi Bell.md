---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ornate handbell creates a sonorous low-pitched tone when rung, as if sounding from a much larger bell than one carried in the hand. The bell is crafted of silver and polished to a reflective sheen, while the bell's wooden handle is carved with detailed images of various foodstuffs. You can Interact with a *jiang-shi bell* to brandish it against a jiang-shi vampire. If a jiang-shi gains the [[Fleeing]] condition as a result of a *jiang-shi bell* being brandished, they must run until they're at least 20 feet away. They take a -2 penalty to the Will save to any attempt to overcome their revulsion toward this object.

**Activate—Phantom Banquet** `pf2:2` (concentrate, manipulate, olfactory, visual)

**Frequency** once per day

**Effect** You ring the bell and create an illusory image of a delicious-looking banquet of food laid out on an altar in a 5-foot-square at any point within 30 feet of you that you can see. Any creature that must eat food to survive that's within 30 feet of the appearance of the illusory food must succeed at a DC 28 [[Will]] save or be so distracted by the food's sight and smell that they become [[Fascinated]] by it for 10 minutes.

This food's appearance can trigger any jiang-shi's bitter epiphany weakness; if the food does so, the jiangshi takes a –2 item penalty to their Will save to resist the effects of this weakness.

**Source:** `= this.source` (`= this.source-type`)
