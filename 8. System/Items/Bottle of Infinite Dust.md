---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Magical]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This plain, faintly green bottle full of sand looks deceptively mundane, though it contains a near endless supply of sand. A very slow but steady stream of sand can be poured from the bottle. Up to 1 pound of sand can be produced a day this way.

**Activate—Grit Geyser** `pf2:2` (earth, manipulate, primal)

**Frequency** once per hour

**Effect** You aim the bottle and unleash a blast of sand. Scouring grit is released in a @Template[type:cone|distance:15], dealing @Damage[4d4[slashing]|options:area-damage] damage to all creatures in the area (DC 23 [[Reflex]] save).

**Activate—Sandstorm** `pf2:3` (earth, manipulate, primal)

**Frequency** once per day

**Effect** You dump out the bottle, creating a swirling sandstorm around you. A @Template[type:emanation|distance:20] is filled with blowing sand that obscures vision. This has the effects of mist. The air within the sandstorm is unbreathable; creatures in the area must hold their breath. Creatures entering or starting their turn in the sandstorm take @Damage[2d4[slashing]|options:area-damage|options:area-effect] damage (DC 23 [[Reflex]] save). Creatures with the water trait or that are primarily made of liquid take double damage. This sandstorm lasts 10 minutes or until the bottle is corked with an Interact action, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
