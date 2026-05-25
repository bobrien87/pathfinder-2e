---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]", "[[Water]]"]
price: "{'gp': 2800}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The beak and talons of a tidehawk form the triggering mechanism of this *+2 greater striking crossbow*. Its grip is constantly damp, though this doesn't affect your ability to keep ahold of the weapon. When used in aquatic combat, a *tidal crossbow* doesn't have its range increments halved. A *tidal crossbow* deals 1d4 additional bludgeoning damage on a successful Strike. On a critical hit, the bow's additional damage is instead 1d4 bludgeoning splash damage, and the target must succeed at a DC 31 [[Reflex]] save or be pushed back 5 feet. The bow critical specialization effect applies to creatures with the water trait even if it wouldn't normally.

**Activate—Typhoon Swell** `pf2:2` (manipulate, water)

**Frequency** once per day

**Effect** The *tidal crossbow* produces a torrent of water in a @Template[line|distance:30], dealing @Damage[8d6[bludgeoning]|options:area-damage] damage (DC 30 [[Fortitude]] save). Creatures that fail the save are also knocked [[Prone]].

**Craft Requirements** The initial raw materials must include the beak, talons, and several watery feathers of a tidehawk.

**Source:** `= this.source` (`= this.source-type`)
