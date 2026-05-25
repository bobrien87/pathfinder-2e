---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Nonlethal]]", "[[Ranged trip]]", "[[Thrown]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This heavy metallic *+1 bola* is a favorite tool of rebels and rabble-rousers against armored opponents. Due to its weight, it has a range increment of 15 feet. When you successfully Strike a creature made of metal or wearing metal armor with this weapon, the bola attaches to the metal and the targeted creature takes a –10-foot circumstance penalty to its Speed until it spends an Interact action to remove the bola.

> [!danger] Effect: Magnetic Bola (Speed Penalty)

**Activate—Overcharge** `pf2:1` (electricity, manipulate, metal)

**Frequency** once per day

**Effect** You overcharge the magnetic properties of the bola. You deal an extra 1d6 electricity damage with your next Strike with this weapon. On a hit, the target must also succeed at a DC 18 [[Reflex]] save or become [[Clumsy]] 1 round (or [[Clumsy]] 2 on a critical failure), in addition to the normal effects. If the target is wearing metal armor, they take a –2 circumstance penalty to their save.

> [!danger] Effect: Magnetic Bola (Damage)

**Craft Requirements** The initial raw materials must include a conductive metal.

**Source:** `= this.source` (`= this.source-type`)
