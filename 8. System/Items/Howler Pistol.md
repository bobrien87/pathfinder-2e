---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Scatter 5]]"]
price: "{'gp': 1100}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Designed by a gunsmith as a personal challenge, a *howler pistol* strikes a miniature version of the *sonic horn* siege weapon's resonating orb with its hammer to generate beams of sonic energy. A *howler pistol* is a *+1 striking dragon mouth pistol* that deals sonic damage instead of piercing damage and doesn't have the concussive trait.

**Activate—Resonant Shatter** `pf2:2` (manipulate)

**Frequency** once per day

**Requirements** The *howler pistol* is loaded

**Effect** You over-torque the *howler pistol*'s hammer to strike the resonating orb harder than normal. The gun fires a concentrated burst of sonic energy that shatters a nearby stone or rock surface, creating a @Template[burst|distance:10] at a point of impact within the gun's first range increment. Creatures in the area take @Damage[5d6[piercing]|options:area-damage] damage (DC 27 [[Reflex]] save).

**Craft Requirements** The initial raw materials must include the powdered horn from a soniphak, processed into a resonating orb.

**Source:** `= this.source` (`= this.source-type`)
