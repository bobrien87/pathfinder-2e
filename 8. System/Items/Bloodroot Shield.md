---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]", "[[Void]]", "[[Wood]]"]
price: "{'gp': 600}"
bulk: "1"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden shield is an interwoven knot of still-living tree roots (Hardness 6, HP 36, BT 18).

**Activate—Thirsty Roots** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You hold out the shield as the roots untangle themselves and launch forward, dealing 9d6 void damage to all creatures in a @Template[line|distance:60] (DC 25 [[Reflex]] save). On a failed save, a creature takes an additional 5 persistent,bleed damage. The shield regains a number of Hit Points equal to half the void damage dealt.

**Source:** `= this.source` (`= this.source-type`)
