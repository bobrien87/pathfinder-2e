---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Trip]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *sinew-song* is an ivory violin bow that bears an odd string, one that vibrates on its own, creating the soft sound of violin music whenever it's swung through the air. When used to play a violin, this ivory bow functions normally but grants a +3 item bonus to any Performance check attempted as a result. It can also be used to mime playing a violin when no instrument is at hand, but in this case, it grants no item bonus to resulting Performance checks.

A *sinew-song's* primary use is as a weapon—it can be wielded as if it were a *+3 keen greater thundering greater striking sickle*.

**Activate—Cutting Cadenza** `pf2:2` (manipulate, sonic)

**Frequency** once per day

**Effect** You Stride once and then swipe the weapon through the air three times. Shimmering waves of sound slice out in a @Template[type:cone|distance:30]. All creatures in the area must attempt a DC 37 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes damage as if you successfully hit it with a Strike using a *sinew-song*, but all of the damage is sonic damage.
- **Failure** As success, but the creature also takes 2d6 persistent,bleed damage.
- **Critical Failure** As success, but double the damage and the creature takes 4d6 persistent,bleed damage.

**Source:** `= this.source` (`= this.source-type`)
