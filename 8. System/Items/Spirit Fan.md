---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Agile]]", "[[Backstabber]]", "[[Deadly d6]]", "[[Finesse]]", "[[Monk]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant black, gold-tipped *+1 striking fighting fan* is adorned with images of three golden leaves and a red rope tassel. If a creature is reduced to 0 Hit Points by a *spirit fan*, the golden leaves on the fan light up, providing illumination equal to that of a torch for 1 minute.

> [!danger] Effect: Spirit Fan

**Activate—Release Life Energy** `pf2:2` (concentrate, manipulate, vitality)

**Requirements** The *spirit fan*'s leaves are illuminated

**Frequency** once per hour

**Effect** You sweep the *spirit fan* in the direction of a single target you can see within 30 feet, releasing the life energy in the form of a streak of golden light. The *spirit fan* goes dark. If the target is a living creature, the energy restores 3d8+8 Hit Points. If the target is undead, it takes @Damage[(2d8+8)[vitality]] damage (DC 23 [[Fortitude]] save).

**Source:** `= this.source` (`= this.source-type`)
