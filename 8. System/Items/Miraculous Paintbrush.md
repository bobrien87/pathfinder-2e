---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 325}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 10 minutes (concentrate, manipulate)

The bristles on a miraculous paintbrush shift in a rainbow of colors, and can magically create an object painted with them. The paint flows as you Activate the miraculous paintbrush and changes color at your whim as you paint. The paint can cover a 10-foot-square, two-dimensional surface. When you're done painting, attempt a DC 30 [[Crafting]] check.
- **Critical Success** The object you painted emerges from the surface as a real, permanent object no larger than 10 feet in any dimension. It's non-magical and inanimate and has no value except to certain art collectors. If you paint a creature, machine, or form of energy (such as a campfire), these depictions appear only as inanimate sculptures. The created object has a painterly appearance that clearly marks its unusual origin, but is as real as any other.
- **Success** As critical success, but the object constantly sheds flakes of paint until it falls apart, destroyed, after 24 hours.
- **Failure** The pigments leave a painting that doesn't quite look right and doesn't become an object.
- **Critical Failure** Is it a dog? Whatever you made is a pretty lousy painting and doesn't resemble what you set out to make.

**Source:** `= this.source` (`= this.source-type`)
