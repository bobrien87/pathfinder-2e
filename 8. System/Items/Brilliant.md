---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]"]
price: "{'gp': 2000}"
usage: "etched-onto-a-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune causes a weapon to transform into pure, brilliant energy. The weapon deals an additional 1d4 fire damage on a successful Strike, as well as 1d4 spirit damage to fiends and 1d4 vitality damage to undead.

On a critical hit, the target must succeed at a DC 29 [[Fortitude]] save or be [[Blinded]] for 1 round.

**Activate—Shine Bright!** `pf2:1` (concentrate, light)

**Effect** You plunge your weapon into darkness to return the light. Attempt a counteract check with a counteract rank of 5 and a +19 counteract modifier to end a magical darkness effect whose area is within reach of the weapon.

**Source:** `= this.source` (`= this.source-type`)
