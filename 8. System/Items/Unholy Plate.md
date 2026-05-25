---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Bulwark]]", "[[Divine]]", "[[Invested]]", "[[Unholy]]"]
price: "{'gp': 2500}"
bulk: "4"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Crafted from black iron, this crude suit of *+2 resilient full plate* is designed to make you look like a horned demon with your face peering out of the screaming maw of the beast.

While wearing the armor, you can attack with the helmet's horns. They're a martial melee weapon with the effects of a +2 weapon potency rune. They deal 2d8 piercing damage and have the deadly d12 and unholy traits. On a critical hit with the horns, the target must succeed at a DC 30 [[Fortitude]] save or become [[Drained]] 1 (or [[Drained]] 2 on a critical failure). The horns can't be etched with any runes.

If you're holy, you're [[Drained]] 2 and can't recover from this condition while wearing unholy plate.

**Activate—Demonic Slip** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You cast [[Translocate]].

**Craft Requirements** You're unholy; supply one casting of *translocate*.

**Source:** `= this.source` (`= this.source-type`)
