---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 85}"
usage: "wornmask"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This black canvas mask covers your mouth and nose, with thick tubes coming from the sides. While wearing this mask, you gain a +1 item bonus to saves against inhaled poisons, inhaled diseases, and olfactory effects.

**Activate—Breathe Clean** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** Your mask springs to life, pumping clean air into your nose and mouth. For 1 round, you are immune to inhaled poisons, inhaled diseases, and olfactory effects. If you have ongoing effects due to such an effect from before activating the mask, those effects continue as normal. If the air around you is unbreathable, you are underwater, or you are in a vacuum, you can breathe normally.

**Source:** `= this.source` (`= this.source-type`)
