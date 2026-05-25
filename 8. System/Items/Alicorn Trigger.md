---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Concussive]]", "[[Fatal aim d12]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking jezail* features a preserved alicorn horn mounted underneath the barrel. Such a horn is usually willingly granted by the creature at the end of its natural lifespan, but some wicked gunsmiths acquire the horn through violence.

**Activate—Glimmer Beam** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The *alicorn trigger* unleashes a beam of radiant light in a @Template[line|distance:60]. Creatures in the area of effect take @Damage[6d6[fire]|options:area-damage] damage and must attempt a DC 33 [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Dazzled]] 1.
- **Failure** The creature takes full damage and is [[Blinded]] for 1 round.
- **Critical Failure** The creature takes double damage and is blinded for 1 minute.

**Craft Requirements** The initial raw materials must include a horn from an alicorn.

**Source:** `= this.source` (`= this.source-type`)
