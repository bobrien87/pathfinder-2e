---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Magical]]"]
price: "{'gp': 23000}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This high-grade adamantine heavy rondache (Hardness 17, HP 100, BT 50) bears a *+3 greater striking shield boss* and has dents that resemble craters on its surface. While wielding the shield, you have fire resistance 15.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You Stride up to three times. This movement doesn't trigger reactions and ignores difficult terrain. At the end of your movement, you deal @Damage[6d10[bludgeoning]|options:area-damage] in a @Template[emanation|distance:10] and @Damage[14d6[fire]|options:area-damage] in a @Template[emanation|distance:40] (DC 40 [[Reflex]] save, with the results applying to both the bludgeoning and fire damage). The space where you end your movement and all adjacent spaces become difficult terrain for 1 minute, and the shield glows red-hot for 10 minutes, during which it gains the effect of the greater flaming property rune.

**Source:** `= this.source` (`= this.source-type`)
