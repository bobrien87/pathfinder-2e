---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 60}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (manipulate)

An alternative to the magical [[Serum of Sex Shift]], euphorium offers similar benefits with a gustatory twist. Euphorium generally takes the form of a light, fluffy cake decorated with overpoweringly sweet frosting and served with alchemically chilled ice cream.

Euphorium's effects begin to manifest as you consume it. With every bite of euphorium, you become a little more yourself. You can pause at any time, halting the transformation midway at a point you choose. In this case, the results persist for 24 hours before reverting slowly over the course of an additional hour, allowing you to approach the experience at your own pace.

The remaining dose of euphorium doesn't spoil (unless it's temporary due to another effect, such as the limitation of Quick Alchemy) but has no effect on anyone other than the person who initially began eating it. This allows you to restart your transformation when you feel comfortable in doing so. Restarting this way quickly restores reverted changes, letting you "pick up where you left off." Once you consume the final bite, the effect functions as if you'd activated a *serum of sex shift*.

**Source:** `= this.source` (`= this.source-type`)
