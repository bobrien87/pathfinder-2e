---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Sonic]]"]
price: "{'gp': 650}"
usage: "wornshoes"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Unassuming in appearance, these slippers indicate their nature only with a signature strip of yellow stitching. You gain a +2 item bonus to Acrobatics checks.

**Activate** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You move like the wind, with precision and speed. You Stride up to 60 feet; this movement doesn't trigger reactions. When you stop, if you've moved at least 30 feet from where you started, you release a thunderous @Template[emanation|distance:5] that deals @Damage[2d6[bludgeoning],2d6[sonic]|options:area-damage]{2d6 bludgeoning damage and 2d6 sonic damage} with a DC 25 [[Fortitude]] save. A creature that critically fails its save is also knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
