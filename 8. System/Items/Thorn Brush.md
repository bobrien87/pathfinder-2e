---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Holy]]", "[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking holy shifting morningstar* has a head that appears to be a deep crimson metal rose with thorny petals. When you activate a *thorn brush* to Shift Weapon, you can cause it to take the shape of a painter's brush. While in this shape, it can't be used as a weapon (it can still be activated to Shift Weapon back into a morningstar), but it does grant a +2 item bonus to Crafting checks to paint or otherwise use the tool while creating artwork.

**Activate—Splatter Paint** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You swing the weapon in an arc, causing a spray of paint of a color of your choice (chosen from black, blue, green, orange, white, or yellow) to splatter all creatures in a @Template[type:cone|distance:30]. Each creature takes 14d6 energy damage based on the color of the paint (14d6 void for black, 14d6 cold for blue, 14d6 acid for green, 14d6 fire for orange, 14d6 vitality for white, or 14d6 electricity for yellow) and must attempt a DC 34 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Dazzled]] by paint in its eyes for 1 minute.
- **Critical Failure** The creature takes double damage and is [[Blinded]] by paint in its eyes for 1 round and then dazzled for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
