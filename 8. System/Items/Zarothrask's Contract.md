---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Contract]]", "[[Invested]]", "[[Occult]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You've bargained for power with a gongorinan, but in return, you must avoid furthering demonic goals. You gain a +2 item bonus to Athletics checks to [[Disarm]] manufactured items and to [[Grapple]]. Once per day, the gongorinan can warp your body with animal features; you must attempt a DC 25 [[Fortitude]] save or become [[Sickened]] 2. When you recover from the sickened condition, your features revert to normal. The gongorinan will usually do this if you sin or aid a demon, even unintentionally.

**Activate—Gongorinan's Emergence** `pf2:2` (concentrate, mental, morph, occult, unholy)

**Frequency** once per day

**Effect** Stony tentacles burst out of your body, lashing at foes. Creatures in a @Template[type:emanation|distance:10] take @Damage[(6d6)[bludgeoning],(2d6)[mental]|options:area-damage] damage (DC 25 [[Fortitude]] save); on a failure, the creature also becomes [[Sickened]] 1 (sickened 2 on a critical failure) as parts of their anatomy temporarily warp into animal features. When a creature recovers from the sickened condition, its features revert to normal.

**Source:** `= this.source` (`= this.source-type`)
